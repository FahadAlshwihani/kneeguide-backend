from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_otp_email(email, otp_code):
    subject = "KneeGuide - Verification Code / رمز التحقق"

    text_content = f"""
Your verification code is: {otp_code}
Valid for 10 minutes.
"""

    html_content = f"""
    <html>
      <body style="font-family:Arial;padding:20px;background:#f5f5f5;">
        <div style="max-width:600px;margin:auto;background:#fff;padding:20px;border-radius:10px;">
          <h2 style="color:#6A0018;text-align:center;">KneeGuide</h2>

          <p style="direction:rtl;text-align:right;">
            رمز التحقق الخاص بك هو:
          </p>
          <h1 style="text-align:center;color:#6A0018;">{otp_code}</h1>
          <p style="direction:rtl;text-align:right;font-size:13px;color:#555;">
            الكود صالح لمدة 10 دقائق.
          </p>

          <hr>

          <p>Hello, your verification code is:</p>
          <h2 style="text-align:center;color:#6A0018;">{otp_code}</h2>
          <p style="font-size:13px;color:#555;">Valid for 10 minutes.</p>

          <br><br>
          <p style="text-align:center;color:gray;font-size:12px;">
            KneeGuide © 2025
          </p>
        </div>
      </body>
    </html>
    """

    msg = EmailMultiAlternatives(
        subject,
        text_content,
        settings.DEFAULT_FROM_EMAIL,
        [email]
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
