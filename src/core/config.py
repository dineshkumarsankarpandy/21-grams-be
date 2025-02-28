import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MyProject"
    SECRET_KEY: str = "SUPERSECRET"           # Should load from env or a secrets manager
    OAUTH_CLIENT_ID: str = "YOUR_CLIENT_ID"   # For SSO
    OAUTH_CLIENT_SECRET: str = "YOUR_SECRET"
    OAUTH_PROVIDER_URL: str = "https://accounts.google.com"  # Example provider

    DATABASE_URL: str = os.getenv("DATABASE_URL")



    AWS_ACCESS_KEY_ID: str = "your-access-key"
    AWS_SECRET_ACCESS_KEY: str = "your-secret-key"
    AWS_S3_REGION: str = "us-east-1"
    AWS_S3_BUCKET: str = "your-bucket-name"

    EMAIL_HOST: str = "smtp.example.com"
    EMAIL_PORT: int = 587
    EMAIL_USER: str = "no-reply@example.com"
    EMAIL_PASSWORD: str = "strongpassword"
    EMAIL_FROM: str = "no-reply@example.com"
    
    TWILIO_ACCOUNT_SID: str = "your_twilio_sid"
    TWILIO_AUTH_TOKEN: str = "your_twilio_auth_token"
    TWILIO_PHONE_NUMBER: str = "+1XXXXXXXXXX"

    FIREBASE_CREDENTIALS_FILE: str = "path/to/firebase_service_account.json"

    STRIPE_SECRET_KEY: str = "sk_test_123"   # from your Stripe dashboard
    STRIPE_WEBHOOK_SECRET: str = "whsec_123" # optional, if you use webhooks

    # For Razorpay, you'd store RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET, etc.
    RAZORPAY_KEY_ID: str = "your_razorpay_key_id"
    RAZORPAY_KEY_SECRET: str = "your_razorpay_key_secret"
    



    class Config:
        env_file = ".env"
        extra = "ignore"



settings = Settings()
