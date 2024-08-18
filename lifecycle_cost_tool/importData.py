from flask import render_template_string, redirect, url_for, request, flash, get_flashed_messages
from jinja2 import Environment, FileSystemLoader
import os
from app import app, db
from app.models import Contract
from app.forms import ContractForm, UploadForm
import pandas as pd
from werkzeug.utils import secure_filename

# Setup the Jinja2 environment to use an absolute path
env = Environment(loader=FileSystemLoader('/'))

def render_template_absolute(template_path, **context):
    # Add Flask-specific functions to the context
    context['url_for'] = url_for
    context['flash'] = flash
    context['get_flashed_messages'] = get_flashed_messages
    template = env.get_template(template_path)
    return template.render(context)

@app.route('/')
def index():
    # Fetch all contracts from the database
    contracts = Contract.query.all()
    
    # Debugging statement to see what contracts are being sent to the template
    print(f"Contracts being sent to template: {contracts}")
    
    # Pass contracts to the template
    return render_template_absolute(r'/Users/owenlin/Desktop/Product Lifecycle App/lifecycle_cost_tool/app/templates/index.html', contracts=contracts)

@app.route('/add', methods=['GET', 'POST'])
def add_contract():
    form = ContractForm()
    if form.validate_on_submit():
        new_contract = Contract(
            year=form.year.data,
            obligation_amount=form.obligation_amount.data,
            description=form.description.data
        )
        db.session.add(new_contract)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template_absolute(r'/Users/owenlin/Desktop/Product Lifecycle App/lifecycle_cost_tool/app/templates/add_contract.html', form=form)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join('uploads', filename)
        
        # Ensure the upload directory exists
        os.makedirs('uploads', exist_ok=True)
        
        form.file.data.save(filepath)

        try:
            # Try reading the CSV without specifying the delimiter or header
            df = pd.read_csv(filepath)

            # Select only the columns you care about
            key_columns = [
                'award_base_action_date_fiscal_year',
                'total_obligated_amount',
                'recipient_name',
                'period_of_performance_start_date',
                'period_of_performance_current_end_date'
            ]
            df_clean = df[key_columns].dropna()

            # Save the cleaned DataFrame to a new CSV file
            output_csv_path = os.path.join('exports', 'cleaned_contracts.csv')
            os.makedirs('exports', exist_ok=True)
            df_clean.to_csv(output_csv_path, index=False)

            flash('Contracts have been successfully uploaded and processed.', 'success')
        except ValueError as e:
            flash(f"Error processing the CSV file: {e}", 'danger')
        except Exception as e:
            flash(f"An unexpected error occurred: {e}", 'danger')

        return redirect(url_for('index'))

    return render_template_absolute(
        r'/Users/owenlin/Desktop/Product Lifecycle App/lifecycle_cost_tool/app/templates/upload.html', 
        form=form
    )




if __name__ == "__main__":
    app.run(debug=True)
