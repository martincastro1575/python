import admin

admin_user = admin.Admin('Martin','Castro','mjcm@gmail.com','CABA')
admin_user.privileges.set_privileges('can add post','can delete post','can ban user',
                                        'can be anything')
admin_user.greet_user()
admin_user.privileges.show_privileges()