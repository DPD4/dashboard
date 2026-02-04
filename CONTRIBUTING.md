# Contributing to Financial Dashboard

نرحب بمساهماتكم في تطوير لوحة التحكم المالية! 

## كيفية المساهمة

### 1. إعداد البيئة التطويرية

```bash
# Clone the repository
git clone https://github.com/yourcompany/financial-dashboard.git
cd financial-dashboard

# Install in development mode
bench get-app /path/to/financial-dashboard
bench --site development.localhost install-app financial_dashboard
```

### 2. إرشادات التطوير

#### Python Code Style
- استخدم PEP 8 لتنسيق الكود
- أضف docstrings للدوال والكلاسات
- استخدم type hints عند الإمكان

```python
def get_financial_data(company: str) -> dict:
    """
    Get financial data for specified company
    
    Args:
        company (str): Company name
        
    Returns:
        dict: Financial data dictionary
    """
    pass
```

#### JavaScript Code Style
- استخدم ES6+ features
- أضف JSDoc comments
- استخدم camelCase للمتغيرات

```javascript
/**
 * Fetch dashboard data from API
 * @param {string} company - Company name
 * @returns {Promise<Object>} Dashboard data
 */
async function fetchDashboardData(company) {
    // Implementation
}
```

#### CSS Guidelines
- استخدم BEM methodology
- دعم RTL layouts
- استخدم CSS custom properties للألوان

```css
.dashboard-card {
    /* Base styles */
}

.dashboard-card--highlighted {
    /* Modifier styles */
}

.dashboard-card__title {
    /* Element styles */
}
```

### 3. إضافة ميزات جديدة

#### إضافة مؤشر مالي جديد

1. أضف الدالة في `dashboard_api.py`:
```python
def get_new_metric(company):
    """Get new financial metric"""
    # Implementation
    return {"value": "100K", "change_percent": 5.2}
```

2. أضف في `get_financial_data()`:
```python
data["new_metric"] = get_new_metric(company)
```

3. أضف في JavaScript:
```javascript
populateNewMetric() {
    const value = this.data.new_metric?.value;
    this.setElementText('newMetricValue', value);
}
```

4. أضف في HTML:
```html
<div class="metric-card">
    <div class="metric-label">المؤشر الجديد</div>
    <div class="metric-value" id="newMetricValue">جاري التحميل...</div>
</div>
```

### 4. إضافة رسم بياني جديد

```javascript
createNewChart() {
    const ctx = document.getElementById('newChart');
    if (!ctx || !this.data?.new_chart_data) return;

    this.charts.newChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: this.data.new_chart_data.labels,
            datasets: [{
                label: 'البيانات الجديدة',
                data: this.data.new_chart_data.data,
                backgroundColor: '#ff4444'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}
```

### 5. إضافة ترجمات

أضف الترجمات في `translations/ar.csv`:
```csv
New Metric,المؤشر الجديد
New Chart,الرسم البياني الجديد
```

### 6. كتابة الاختبارات

```python
def test_new_metric(self):
    """Test new metric calculation"""
    result = get_new_metric("Test Company")
    
    self.assertIsInstance(result, dict)
    self.assertIn("value", result)
    self.assertIn("change_percent", result)
```

### 7. تحديث الوثائق

- أضف وصف الميزة الجديدة في README.md
- أضف أمثلة الاستخدام
- حدث API documentation

## إرشادات Pull Request

### قبل إرسال PR

1. **تأكد من الاختبارات**:
```bash
bench --site development.localhost run-tests --app financial_dashboard
```

2. **تحقق من Code Style**:
```bash
flake8 financial_dashboard/
```

3. **اختبر على بيانات حقيقية**:
```bash
bench --site development.localhost execute financial_dashboard.api.dashboard_api.get_financial_data
```

### عنوان PR

استخدم تنسيق واضح:
- `feat: إضافة مؤشر الربحية الجديد`
- `fix: إصلاح خطأ في حساب التدفق النقدي`
- `docs: تحديث دليل التثبيت`
- `style: تحسين تنسيق الكود`
- `refactor: إعادة هيكلة API endpoints`

### وصف PR

```markdown
## الوصف
وصف مختصر للتغييرات

## نوع التغيير
- [ ] إصلاح خطأ (bug fix)
- [ ] ميزة جديدة (new feature)
- [ ] تغيير مؤثر (breaking change)
- [ ] تحديث وثائق (documentation update)

## الاختبار
- [ ] تم اختبار الكود محلياً
- [ ] تم تشغيل الاختبارات الآلية
- [ ] تم اختبار على بيانات حقيقية

## لقطات الشاشة (إن وجدت)
أضف لقطات شاشة للتغييرات المرئية
```

## معايير المراجعة

### Code Quality
- ✅ الكود يتبع المعايير المحددة
- ✅ لا توجد أخطاء syntax
- ✅ الدوال موثقة بشكل جيد
- ✅ معالجة الأخطاء موجودة

### Functionality
- ✅ الميزة تعمل كما هو متوقع
- ✅ لا تؤثر على الميزات الموجودة
- ✅ تعمل مع الشركات المتعددة
- ✅ تدعم اللغة العربية

### Performance
- ✅ لا تؤثر على أداء النظام
- ✅ استعلامات قاعدة البيانات محسنة
- ✅ تستخدم cache عند الحاجة

### Security
- ✅ تتبع معايير الأمان
- ✅ تستخدم frappe.whitelist() للـ API
- ✅ تتحقق من الصلاحيات

## الحصول على المساعدة

- 📧 البريد الإلكتروني: dev@yourcompany.com
- 💬 Discord: [رابط الخادم]
- 📖 الوثائق: [docs.yourcompany.com](https://docs.yourcompany.com)

## شكر وتقدير

شكراً لكم على مساهماتكم في تطوير هذا المشروع! 🙏