import numpy as np

# Infraestructure
from infraestructure.init import get_dataframe
from infraestructure.get_filters_options import get_filters_options
from infraestructure.get_sliders_options import get_sliders_options
from infraestructure.filter_dataset import filter_dataset
from infraestructure.get_metrics import get_metrics
from infraestructure.get_charts_data import get_charts_data
from infraestructure.get_top_5 import get_top_5
from infraestructure.get_statistical_summary import get_statistical_summary

# Presentation
import presentation.set_page_config
from presentation.show_dataset import show_dataset
from presentation.show_title import show_title
from presentation.create_multiselect_filters import create_multiselect_filters
from presentation.create_sliders import create_sliders
from presentation.show_metrics import show_metrics
from presentation.show_charts import show_charts
from presentation.export_top_5 import export_top_5
from presentation.show_statistical_summary import show_statistical_summary

df = get_dataframe()

student_options, blood_type_options, hair_color_options, neightborhood_options = get_filters_options( df )
students_full_name = student_options.get('full_name')
students_code = student_options.get('code')

age_range_options, height_range_options = get_sliders_options( df )

selected_students, selected_blood_types, selected_hair_colors, selected_neightborhoods = create_multiselect_filters( students_full_name, blood_type_options, hair_color_options, neightborhood_options )

selected_age, selected_height = create_sliders( age_range_options, height_range_options )

students_index = [ np.where( students_full_name == selected_students[i] )[0] for i in range( len( selected_students ) ) ] if len( selected_students ) > 0 else []
selected_students_code = students_code[ students_index ].flatten()

df = filter_dataset( {
    'selected_students': selected_students_code, 
    'selected_blood_type': selected_blood_types,
    'selected_hair_color': selected_hair_colors, 
    'selected_neightborhood': selected_neightborhoods,
    'selected_age': selected_age,
    'selected_height': selected_height
}, df )

show_title()

show_dataset( df )

metrics = get_metrics( df )
show_metrics( metrics )

# graficos filas 1, 2 y 3
charts_data = get_charts_data(df, age_bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
show_charts(charts_data)

# top 5
top_5_data = get_top_5(df)
export_top_5(top_5_data)

# resumen estadístico
statistical_summary = get_statistical_summary(df)
show_statistical_summary(statistical_summary)