from django.urls import path


from clients.views import (create_client, list_client,
                           delete_client, edit_client, export_data)


urlpatterns = [
    path('', list_client.ListClientView.index, name='all_client'),
    path('create/', create_client.CreateClientView.create, name='create_client'),
    path('save/', create_client.CreateClientView.save, name='save_client'),
    path('delete/<int:client_id>',
         delete_client.DeleteClientView.delete, name='delete_client'),
    path('detail/<int:client_id>',
         list_client.ListClientView.detail, name='detail_client'),
    path('edit/<int:client_id>', edit_client.EditClientView.edit, name='edit_client'),
    path('update/<int:client_id>',
         edit_client.EditClientView.update, name='update_client'),
    path('export',
         export_data.export, name='export_data')
]
