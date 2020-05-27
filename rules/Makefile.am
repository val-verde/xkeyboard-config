SUBDIRS = compat

if CREATE_RULES_SYMLINK
#  extra_rules_file = $(xkb_rules_symlink)
#  extra_dir_file   = $(extra_rules_file).xml 
#  extra_lst_file   = $(extra_rules_file).lst

install-data-hook:
	for file in `echo "$(xkb_rules_symlink)" | sed 's/,/ /'` ; do \
		extra_rules_file=$$file ; \
		extra_dir_file=$$extra_rules_file.xml ; \
		extra_lst_file=$$extra_rules_file.lst ; \
		ln -sf base     $(DESTDIR)$(rulesdir)/$$extra_rules_file ; \
		ln -sf base.lst $(DESTDIR)$(rulesdir)/$$extra_lst_file ; \
		ln -sf base.xml $(DESTDIR)$(rulesdir)/$$extra_dir_file ; \
	done

else
install-data-hook:

endif

parts = \
	0000-base.hdr.part \
	0001-base.lists.part \
	0002-RULESET.lists.base.part \
	0004-RULESET.m_k.part \
	0005-base.l1_k.part \
	0006-base.l_k.part \
	0007-base.o_k.part \
	0008-base.ml_g.part \
	0009-base.m_g.part \
	0011-base.mlv_s.part \
	0013-base.ml_s.part \
	0015-base.ml1_s.part \
	0018-base.ml2_s.part  \
	0020-base.ml3_s.part  \
	0022-base.ml4_s.part  \
	0026-RULESET.m_s.part \
	0027-RULESET.ml_s1.part \
	0033-base.ml_c.part \
	0034-base.ml1_c.part \
	0035-base.m_t.part \
	0036-base.lo_s.part \
	0037-base.l1o_s.part \
	0038-base.l2o_s.part \
	0039-base.l3o_s.part \
	0040-base.l4o_s.part \
	0042-base.o_s.part \
	0043-base.o_c.part \
	0044-base.o_t.part

compat_parts = \
	compat/0003-base.lists.part \
	compat/0010-base.mlv_s.part \
	compat/0012-base.ml_s.part \
	compat/0014-base.ml1_s.part \
	compat/0016-base.ml1v1_s.part \
	compat/0017-base.ml2_s.part \
	compat/0019-base.ml3_s.part \
	compat/0021-base.ml4_s.part \
	compat/0023-base.ml2v2_s.part  \
	compat/0024-base.ml3v3_s.part  \
	compat/0025-base.ml4v4_s.part  \
	compat/0028-base.lv_c.part   \
	compat/0029-base.l1v1_c.part \
	compat/0030-base.l2v2_c.part \
	compat/0031-base.l3v3_c.part \
	compat/0032-base.l4v4_c.part \
	compat/0041-base.o_s.part

if USE_COMPAT_RULES
parts += $(compat_parts)
endif

rules_files = base evdev xfree98

lst_files = base.lst evdev.lst

SUFFIXES = .xml .lst

.xml.lst:
	perl $(srcdir)/xml2lst.pl < $< > $@

base_parts=$(subst RULESET,base,$(parts))
base: $(base_parts) merge.py
	$(srcdir)/merge.py $@ $(srcdir) $(builddir) $(base_parts)

evdev_parts=$(subst RULESET,evdev,$(parts))
evdev: $(evdev_sources) merge.py
	$(srcdir)/merge.py $@ $(srcdir) $(builddir) $(evdev_parts)

dist_files = xkb.dtd README

rules_DATA = $(rules_files) $(lst_files) $(dist_files)

xml_DATA = base.xml evdev.xml base.extras.xml evdev.extras.xml

$(srcdir)/evdev.xml: base.xml
	cp $(srcdir)/base.xml $@

$(srcdir)/evdev.extras.xml: base.extras.xml
	cp $(srcdir)/base.extras.xml $@

EXTRA_DIST= $(xml_DATA) xfree98 \
            $(base_parts) $(evdev_parts) $(compat_parts) \
            xml2lst.pl merge.py xkb.its $(dist_files)

CLEANFILES = base base.lst evdev evdev.lst

rulesdir = $(xkb_base)/rules
xmldir = $(rulesdir)
