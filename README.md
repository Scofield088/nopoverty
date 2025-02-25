# No Poverty Project


## 🌍 About the Project
The **No Poverty** project is a web-based application designed to combat poverty by leveraging technology to connect people in need with resources, volunteers, donations, and microfinance opportunities. The platform provides tools to facilitate aid distribution, encourage volunteer participation, and offer financial assistance.

## 🚀 Features
- 🔹 **Donation System** – Secure transactions using Razorpay
- 🔹 **Aid Locator** – Helps users find resources and assistance nearby
- 🔹 **Microfinance Support** – Connects individuals with microfinance opportunities
- 🔹 **Volunteer Network** – Enables people to offer help and support
- 🔹 **AI Suggestions** – Uses AI-powered recommendations to suggest resources
- 🔹 **Food Distribution** – Ensures food security for those in need
- 🔹 **Interactive Map** – Visual representation of aid centers and donation hubs

## 🛠️ Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django (Python)
- **Database:** SQLite (can be switched to PostgreSQL or MySQL)
- **Payment Gateway:** Razorpay
- **Version Control:** Git & GitHub
- **Deployment:** (Mention if deployed, e.g., AWS, Heroku, etc.)

## 📦 Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Scofield088/nopoverty.git
   cd nopoverty
   ```
2. Create a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the project root and add:
     ```env
     GEMINI_API_KEY=your_gemini_api_key_here
     RAZORPAY_KEY_ID=your_razorpay_key_id_here
     RAZORPAY_KEY_SECRET=your_razorpay_secret_here
     ```
5. Run migrations:
   ```sh
   python manage.py migrate
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```

## 📌 Usage
- Users can register and log in to access various features.
- Donors can contribute funds via Razorpay.
- Volunteers can sign up and offer services.
- AI-based suggestions help users find relevant aid.
- The interactive map helps locate nearby resources.




---
**Together, we can make a difference! 🌍**
