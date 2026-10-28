
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings

from .models import product, monthlydeal, logo,contactforms
from django.contrib import messages
from google import genai
from google.genai.errors import ServerError

from pathlib import Path
from pypdf import PdfReader

import os
import time


# -----------------------------
# WEBSITE PAGE VIEWS
# -----------------------------

def home(request):
    productsdata = product.objects.all()
    monthdata = monthlydeal.objects.first()
    logodata = logo.objects.all()

    context = {
        'product': productsdata,
        'monthlydeal': monthdata,
        'logo': logodata,
    }

    return render(request, 'index.html', context)


def home2(request):
    return render(request, 'index2.html')


def about(request):
    return render(request, 'about.html')


def news(request):
    return render(request, 'news.html')


def contact(request):
     print("CONTACT VIEW FILE:", __file__)

     if request.method=="POST":
        name=request.POST.get("name","").strip()
        email=request.POST.get("email","").strip()
        phone=request.POST.get("phone","").strip()
        subject=request.POST.get("subject","").strip()
        message_text=request.POST.get("message","").strip()

        if name and email and subject and message_text:
            contactforms.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message_text,
            )
            messages.success(
                request,
                "Thank you!, your message has been submitted"
                )
            return redirect("/#contact")
        messages.error(
            request,
            "please fill in all contact form fields."
            )
     return render(request, 'contact.html')


def shop(request):
    return render(request, 'shop.html')


def page404(request):
    return render(request, '404.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def singlenews(request):
    return render(request, 'singlenews.html')


def singleproduct(request):
    return render(request, 'singleproduct.html')


# -----------------------------
# PDF-BASED GEMINI CHATBOT
# -----------------------------

@require_POST
def chatbot_api(request):

    # Get the customer's question
    question = request.POST.get("message", "").strip()

    if not question:
        return JsonResponse(
            {"error": "Please enter a question."},
            status=400
        )

    if len(question) > 1000:
        return JsonResponse(
            {
                "error": "Please keep your question under 1000 characters."
            },
            status=400
        )

    # Get Gemini API key
    api_key = os.environ.get("GOOGLE_API_KEY")

    if not api_key:
        return JsonResponse(
            {
                "error": "AI API key is not configured on the server."
            },
            status=500
        )

    try:
        # Find the PDF in the knowledge folder
        pdf_path = (
            Path(settings.BASE_DIR)
            / "knowledge"
            / "frutika_info.pdf"
        )

        # Check whether the PDF exists
        if not pdf_path.exists():
            print("PDF NOT FOUND:", pdf_path)

            return JsonResponse(
                {
                    "error": (
                        "Frutika knowledge PDF was not found. "
                        "Please check the knowledge folder."
                    )
                },
                status=500
            )

        # Read text from the PDF
        reader = PdfReader(str(pdf_path))
        website_info = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                website_info.append(page_text)

        context = "\n".join(website_info)

        if not context.strip():
            return JsonResponse(
                {
                    "error": (
                        "No readable text was found in the PDF."
                    )
                },
                status=500
            )

        # Connect to Gemini
        client = genai.Client(api_key=api_key)

        # Retry temporary Gemini server errors up to 3 times
        for attempt in range(3):

            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=(
                        "You are a helpful customer support assistant "
                        "for the Frutika website.\n\n"

                        "Use the supplied PDF as your knowledge base.\n"
                        "Answer questions about products, prices, "
                        "monthly deals and website services using "
                        "only information supported by the PDF.\n"
                        "Do not invent product names, prices, stock "
                        "availability, delivery details or offers.\n"
                        "If the information is missing from the PDF, "
                        "say that you cannot confirm it from the "
                        "available information.\n\n"

                        f"FRUTIKA PDF INFORMATION:\n{context}\n\n"
                        f"CUSTOMER QUESTION:\n{question}"
                    )
                )

                answer = response.text

                if not answer:
                    return JsonResponse(
                        {
                            "error": (
                                "The AI returned an empty response. "
                                "Please try again."
                            )
                        },
                        status=503
                    )

                return JsonResponse({
                    "answer": answer
                })

            except ServerError:
                if attempt == 2:
                    raise

                # Wait before retrying
                time.sleep(3)

    except Exception as e:
        import traceback

        traceback.print_exc()
        print("GEMINI CHATBOT ERROR:", repr(e))

        return JsonResponse(
            {
                "error": (
                    "Sorry, the AI assistant is temporarily busy "
                    "or the knowledge PDF could not be processed. "
                    "Please try again later."
                )
            },
            status=503
        )
