
commit_params = ncs.maapi.CommitParams()
commit_params.dry_run_cli()
commit = t.apply_params(True, commit_params)
print("Commiting Dry-Run NSO CLI Style: ")
print(commit)
print (commit.get("local-node"))