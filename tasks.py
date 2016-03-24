from atelier.tasks import ns, setup_from_tasks

setup_from_tasks(globals(), "commondata")
ns.configure({
    'revision_control_system': 'git',
    'doc_trees': [],
})
