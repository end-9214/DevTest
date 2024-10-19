import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from django.core.mail import EmailMessage
from django.shortcuts import render

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        df = pd.DataFrame()

        try:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file, encoding='utf-8')
            elif file.name.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file)
            else:
                return render(request, 'upload.html', {'error': 'Unsupported file type.'})
        except UnicodeDecodeError:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file, encoding='ISO-8859-1')
            else:
                return render(request, 'upload.html', {'error': 'Error reading the file.'})

        df = df.dropna()
        
        total_records = len(df)
        total_columns = df.shape[1]
        column_names = df.columns.tolist()
        
        summary_df = df.head()
        summary = summary_df.to_html()
        
        excel_file = BytesIO()
        summary_df.to_excel(excel_file, index=False)
        excel_file.seek(0)

        fig, ax = plt.subplots(figsize=(8, 2))
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=summary_df.values, colLabels=summary_df.columns, cellLoc='center', loc='center')
        plt.title('Summary Report')
        img_data = BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)
        email_body = (
            f'Total Records: {total_records}\n'
            f'Total Columns: {total_columns}\n'
            f'Column Names: {", ".join(column_names)}'
        )

        email = EmailMessage(
            'Summary Report',
            email_body,
            'karamveersingh2003111@gmail.com',
            ['tech@themedius.ai']
        )
        email.attach('summary_report.xlsx', excel_file.read(), 'application/vnd.ms-excel')
        email.attach('summary_image.png', img_data.read(), 'image/png')
        email.send()

        return render(request, 'upload.html', {'summary': summary, 'total_records': total_records})

    return render(request, 'upload.html')
