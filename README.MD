پروژه Web Scraping
---

برنامه‌ای بنویسید که از سایت Truecar قیمت و میزان کارکرد ۲۰ نفر اولی که یک ماشین دلخواه (اسم ماشین در ورودی داده می‌شود) را می‌فروشند بگیرد و در یک دیتابیس دلخواه ذخیره کند.


*** راه حل ***
ابتدا دیتابیس مورد نظر را تشکیل می‌دهیم (فایل های DB_Setup و Database)
بیاد داشته باشیم که در زمان اجرا روی سیستم های متفاوت نیاز به اصلاح بخش کانفیک اسکریپت های دیتابیس داری (یوزر و پسور خود را وارد کنید)

 سپس با کمک کتابخانه requstes به وب سایت مورد نظر درخواست میزنیم و سپس درخواست مورد نظر را با Beautiful از کتابخانهbs4 ابتدا پارس میکنیم .
سپس با جستجو موارد مورند نظرمان با کمک تگ های اچ‌تی‌ام‌ای پیدا و در دیتابیس ذخیر میکنیم.
می‌توانیم اطلاعات موجود را در یک فایل csv نیز ذخیر کنیم که این قسمت کد بدون استفاده از contex manger انجام و کامنت شد.

** توجه**
لازم به توضیح است که در صورت request مرتب و یا وارد کردن اشتباه نام تولید کننده، امکان بن شدن از طریق وب سایت زیاد است. 
این مشکل برای کسانی که از dynamic ip استفاده میکنن بیشتر هم هست. چرا که سیستم CloudFront اون ip بن می‌کند  و تا مدتی قابلیت استفاده از وب سایت و ریکوئست زدن رو نخواهد داشت.