_default:
	@echo "make"
sources:
	@echo "make sources"
srpm: sources
	rpmbuild -bs --define '_sourcedir .' --define '_srcrpmdir .' fermilab-base_on-site.spec
