# Max Branding Update - به‌روزرسانی برندینگ Max

## تغییرات اعمال شده

### 1. تغییر نام سایت به "Max"

- ✅ تغییر title در تمام صفحات
- ✅ تغییر navbar brand
- ✅ تغییر footer copyright
- ✅ تغییر sidebar footer
- ✅ تغییر base.html title template

### 2. حذف لوگو و اضافه کردن آیکون تاج

- ✅ حذف تصویر لوگو از navbar
- ✅ اضافه کردن آیکون تاج با گرادیانت طلایی
- ✅ طراحی مدرن با shadow و border-radius

### 3. آیکون‌های خفن برای صفحه Index

- ✅ **Web Development**: آیکون کد با گرادیانت آبی
- ✅ **UI/UX Design**: آیکون پالت با گرادیانت صورتی
- ✅ **AI & Automation**: آیکون ربات با گرادیانت بنفش
- ✅ **E-Commerce Platform**: آیکون سبد خرید با گرادیانت سبز
- ✅ **AI Dashboard**: آیکون چارت با گرادیانت نارنجی
- ✅ **Portfolio Platform**: آیکون کیف با گرادیانت قرمز

### 4. حذف فرم اضافه کردن پروژه

- ✅ حذف کامل فرم Add New Project از صفحه projects.html
- ✅ حذف JavaScript مربوط به AJAX submission
- ✅ تمیز کردن کد و حذف فضاهای اضافی

### 5. ایجاد صفحه پروژه‌ها در داشبورد

- ✅ ایجاد `templates/dashboard.html`
- ✅ طراحی مدرن با استایل رادیانت متحرک
- ✅ کارت‌های آماری پروژه‌ها
- ✅ Grid layout برای نمایش پروژه‌ها
- ✅ Modal برای اضافه کردن پروژه جدید
- ✅ آیکون‌های FontAwesome برای تمام المان‌ها

## ویژگی‌های صفحه پروژه‌ها

### آمار پروژه‌ها

- **Total Projects**: 12 پروژه
- **Completed**: 8 پروژه تکمیل شده
- **In Progress**: 3 پروژه در حال انجام
- **On Hold**: 1 پروژه متوقف

### کارت‌های پروژه

- طراحی شفاف با backdrop-filter
- انیمیشن hover و transition
- Badge های رنگی برای وضعیت
- دکمه‌های ویرایش و حذف
- نمایش تکنولوژی‌ها
- تاریخ سررسید

### Modal اضافه کردن پروژه

- فرم کامل با validation
- فیلدهای: عنوان، توضیحات، تکنولوژی‌ها، وضعیت، تاریخ سررسید
- طراحی مدرن با شفافیت
- JavaScript برای مدیریت فرم

## فایل‌های ایجاد/تغییر یافته

### فایل‌های جدید:

1. `templates/projects-dashboard.html` - صفحه پروژه‌ها در داشبورد
2. `static/css/projects-dashboard.css` - استایل‌های خاص صفحه پروژه‌ها
3. `MAX_BRANDING_UPDATE.md` - این فایل مستندات

### فایل‌های تغییر یافته:

1. `templates/dashboard.html` - اضافه کردن لینک پروژه‌ها
2. `templates/index.html` - آیکون‌های جدید
3. `templates/projects.html` - حذف فرم اضافه کردن پروژه
4. `templates/base.html` - تغییر لوگو و اضافه کردن FontAwesome

## آیکون‌های استفاده شده

### FontAwesome Icons:

- `fa-crown` - لوگو Max
- `fa-code` - Web Development
- `fa-palette` - UI/UX Design
- `fa-robot` - AI & Automation
- `fa-shopping-cart` - E-Commerce
- `fa-chart-line` - AI Dashboard
- `fa-briefcase` - Portfolio
- `fa-project-diagram` - Projects Menu
- `fa-plus` - Add Project Button
- `fa-edit` - Edit Project
- `fa-trash` - Delete Project

## رنگ‌بندی

### گرادیانت‌های آیکون‌ها:

- **آبی**: `from-blue-500 to-blue-600`
- **صورتی**: `from-pink-500 to-pink-600`
- **بنفش**: `from-purple-500 to-purple-600`
- **سبز**: `from-green-500 to-green-600`
- **نارنجی**: `from-orange-500 to-orange-600`
- **قرمز**: `from-red-500 to-red-600`
- **طلایی**: `from-yellow-400 to-orange-500` (لوگو)

### Badge Colors:

- **Success**: `#10b981` (تکمیل شده)
- **Warning**: `#f59e0b` (در حال انجام)
- **Info**: `#3b82f6` (متوقف)
- **Primary**: `#667eea` (تکنولوژی‌ها)

## Responsive Design

### Breakpoints:

- **Mobile**: < 576px
- **Tablet**: < 768px
- **Desktop**: > 768px

### ویژگی‌های Responsive:

- Grid layout تطبیقی
- Modal responsive
- Font size های متغیر
- Padding و margin های تطبیقی

## JavaScript Features

### عملکردهای اضافه شده:

- `addProject()` - اضافه کردن پروژه جدید
- `getStatusColor()` - دریافت رنگ وضعیت
- `getStatusText()` - دریافت متن وضعیت
- مدیریت Modal
- Validation فرم

## نکات فنی

### CSS Features:

- `backdrop-filter: blur()` برای شفافیت
- `transform` و `transition` برای انیمیشن
- `gradient` برای رنگ‌بندی
- `box-shadow` برای عمق
- `border-radius` برای گوشه‌های گرد

### Performance:

- استفاده از CSS transforms به جای position changes
- Lazy loading برای تصاویر
- بهینه‌سازی انیمیشن‌ها
- Minification CSS

---

**توسعه‌دهنده**: Amiryousef Tousi  
**تاریخ**: 2025  
**نسخه**: 5.3
**برند**: Max
