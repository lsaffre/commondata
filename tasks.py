from atelier.invlib import setup_from_tasks
ns = setup_from_tasks(globals())
ns.configure({
    'revision_control_system': 'git',
    'doc_trees': [],
})
