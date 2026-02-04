# 🚀 تثبيت من GitHub - دليل شامل

## 📋 المتطلبات المسبقة

- **ERPNext 15.x** مثبت ويعمل
- **Ubuntu 24.04 LTS** (مُوصى به)
- **Frappe Bench** مُعد بشكل صحيح
- **Git** مثبت على النظام

## 🔧 خطوات التثبيت من GitHub

### الخطوة 1: الانتقال إلى مجلد Frappe Bench
```bash
cd ~/frappe-bench
```

### الخطوة 2: تحميل التطبيق من GitHub
```bash
bench get-app https://github.com/DPD4/financial-dashboard-erpnext.git
```

### الخطوة 3: تثبيت التطبيق على الموقع
```bash
bench --site your-site.com install-app financial_dashboard_final
```

### الخطوة 4: ترحيل قاعدة البيانات
```bash
bench --site your-site.com migrate
```

### الخطوة 5: مسح الذاكرة المؤقتة وإعادة التشغيل
```bash
bench clear-cache
bench restart
```

## ✅ التحقق من نجاح التثبيت

### 1. فحص قائمة التطبيقات
```bash
bench --site your-site.com list-apps
```
**يجب أن ترى:** `financial_dashboard_final` في القائمة

### 2. اختبار API
```bash
curl "http://your-site.com/api/method/financial_dashboard_final.financial_dashboard_final.api.test_connection"
```

**الاستجابة المتوقعة:**
```json
{
  "message": {
    "status": "working",
    "message": "لوحة التحكم المالية تعمل بنجاح! 🎉",
    "version": "1.0.0"
  }
}
```

### 3. فحص Workspaces
- ادخل إلى ERPNext
- ابحث عن "Financial" في الشريط الجانبي
- يجب أن ترى 4 workspaces جديدة:
  - نظرة عامة مالية
  - تحليلات المبيعات
  - إدارة المخزون
  - التحليلات المتقدمة

### 4. اختبار صفحات Dashboard
زيارة هذه الروابط:
- `http://your-site.com/financial-overview`
- `http://your-site.com/sales-analytics`
- `http://your-site.com/inventory-management`
- `http://your-site.com/advanced-analytics`

## 🔍 استكشاف الأخطاء

### خطأ 1: "Repository not found"
```bash
# تأكد من صحة رابط GitHub
git ls-remote https://github.com/DPD4/financial-dashboard-erpnext.git
```

### خطأ 2: "App already exists"
```bash
# احذف التطبيق الموجود أولاً
bench --site your-site.com uninstall-app financial_dashboard_final
rm -rf apps/financial_dashboard_final
# ثم أعد التثبيت
bench get-app https://github.com/DPD4/financial-dashboard-erpnext.git
```

### خطأ 3: "Permission denied"
```bash
# إصلاح الأذونات
sudo chown -R $USER:$USER apps/financial_dashboard_final/
chmod -R 755 apps/financial_dashboard_final/
```

### خطأ 4: "Module not found"
```bash
# تأكد من وجود الملفات المطلوبة
ls apps/financial_dashboard_final/
ls apps/financial_dashboard_final/financial_dashboard_final/

# أعد تشغيل النظام
bench restart
```

### خطأ 5: "Database migration failed"
```bash
# فحص سجلات الأخطاء
tail -f logs/bench.log

# إعادة محاولة الترحيل
bench --site your-site.com migrate --skip-failing
```

## 🔄 تحديث التطبيق

### تحديث من GitHub
```bash
cd ~/frappe-bench
bench update --app financial_dashboard_final
```

### تحديث يدوي
```bash
cd apps/financial_dashboard_final
git pull origin main
cd ~/frappe-bench
bench --site your-site.com migrate
bench restart
```

## 🗑️ إلغاء التثبيت

```bash
# إلغاء تثبيت التطبيق
bench --site your-site.com uninstall-app financial_dashboard_final

# حذف ملفات التطبيق
rm -rf apps/financial_dashboard_final

# إعادة تشغيل النظام
bench restart
```

## 📊 ما ستحصل عليه بعد التثبيت

### 🏗️ Workspaces في ERPNext Desk
- **4 workspaces جديدة** تظهر في الشريط الجانبي
- **Number cards** تعرض بيانات مالية حقيقية
- **Shortcuts** للوصول السريع للـ DocTypes
- **Links** لصفحات Dashboard

### 📱 صفحات Dashboard
- **5 صفحات كاملة** بتصميم عربي RTL
- **رسوم بيانية تفاعلية** باستخدام Chart.js
- **تحديث تلقائي** كل 5 دقائق
- **تصميم متجاوب** يعمل على جميع الأجهزة

### 🔌 API Endpoints
- **25+ endpoint** للبيانات المالية
- **تكامل حقيقي** مع قاعدة بيانات ERPNext
- **معالجة أخطاء** شاملة
- **بيانات احتياطية** عند الحاجة

## 🎯 نصائح للاستخدام الأمثل

### 1. إعداد البيانات الأساسية
- تأكد من وجود حسابات مالية في دليل الحسابات
- أدخل بعض فواتير المبيعات للاختبار
- أضف أصناف وحركات مخزون

### 2. إعداد الصلاحيات
- امنح المستخدمين صلاحيات الوصول للـ Workspaces
- حدد الأدوار المناسبة لكل مستخدم

### 3. تخصيص التطبيق
- عدّل ألوان الـ Number Cards من ملفات Workspace
- أضف shortcuts إضافية حسب الحاجة
- خصص API endpoints للمتطلبات الخاصة

## 📞 الحصول على المساعدة

إذا واجهت أي مشاكل:

1. **تحقق من سجلات الأخطاء:**
   ```bash
   tail -f logs/bench.log
   ```

2. **اختبر الاتصال بقاعدة البيانات:**
   ```bash
   bench --site your-site.com console
   >>> import frappe
   >>> frappe.db.sql("SELECT 1")
   ```

3. **تحقق من حالة ERPNext:**
   ```bash
   bench --site your-site.com console
   >>> import frappe
   >>> frappe.get_all("Sales Invoice", limit=1)
   ```

4. **أنشئ issue على GitHub:**
   [GitHub Issues](https://github.com/DPD4/financial-dashboard-erpnext/issues)

---

**التثبيت من GitHub مضمون العمل! 🎉**