import numpy as np

# Infraestructure
from infraestructure.init import get_dataframe
from infraestructure.get_filters_options import get_filters_options
from infraestructure.get_sliders_options import get_sliders_options
from infraestructure.filter_dataset import filter_dataset
from infraestructure.get_metrics import get_metrics
from infraestructure.save_top_five import save_top_five

# Presentation
import presentation.set_page_config
from presentation.show_dataset import show_dataset
from presentation.show_title import show_title
from presentation.create_multiselect_filters import create_multiselect_filters
from presentation.create_sliders import create_sliders
from presentation.show_metrics import show_metrics
from presentation.show_charts import show_all_charts
from presentation.show_summary_stats import show_summary_stats
from presentation.show_download_top_five import show_download_top_five

show_title()

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

show_dataset( df )

metrics = get_metrics( df )
show_metrics( metrics )

show_all_charts( df )

show_summary_stats( df )

save_top_five( df )

show_download_top_five( df )