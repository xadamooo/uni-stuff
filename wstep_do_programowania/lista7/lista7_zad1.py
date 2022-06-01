import lista7_module
import lista7_module as module_1
from lista7_module import Admin as adm

admin_1 = lista7_module.Admin('Admin', 'Admiński', 0,
                              'haselko312', '2002-10-10')
admin_1.show_privileges()

admin_2 = module_1.Admin('Admin', 'Admiński', 0,
                         'haselko312', '2002-10-10')
admin_2.show_privileges()

admin_3 = adm('Admin', 'Admiński', 0,
              'haselko312', '2002-10-10')
admin_3.show_privileges()
