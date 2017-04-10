import importlib
import pkgutil

from init_celery import app

print "registering tasks ..."
list_all_mods = []

for mod in pkgutil.walk_packages("."):
    if "celery_tasks.tasks" in mod[1]:
        if not mod[2]:
            list_all_mods.append(mod[1])
for module_full_path in list_all_mods:
    print module_full_path
    importlib.import_module(module_full_path)
print [repr(reg_task) for reg_task in app.tasks]\

celery_app = app