layout_mappings=$(srcdir)/layoutsMapping.lst
variant_mappings=$(srcdir)/variantsMapping.lst

dist_parts= \
    0041-base.o_s.part \
    0028-base.lv_c.part \
    0029-base.l1v1_c.part \
    0030-base.l2v2_c.part \
    0031-base.l3v3_c.part \
    0032-base.l4v4_c.part

scripts= \
    0017-base.ml2_s.part \
    0019-base.ml3_s.part \
    0021-base.ml4_s.part \
    0023-base.ml2v2_s.part \
    0024-base.ml3v3_s.part \
    0025-base.ml4v4_s.part \
    0012-base.ml_s.part \
    0014-base.ml1_s.part \
    0010-base.mlv_s.part \
    0016-base.ml1v1_s.part

if USE_COMPAT_RULES

noinst_SCRIPTS=$(scripts) $(dist_parts)

else

noinst_SCRIPTS=

endif

0014-base.ml1_s.part: map-variants.py $(layout_mappings) $(variant_mappings)
	$(srcdir)/map-variants.py --want=mls --number=1 $@ $(layout_mappings) $(variant_mappings)

0017-base.ml2_s.part: map-variants.py $(layout_mappings) $(variant_mappings)
	$(srcdir)/map-variants.py --want=mls --number=2 $@ $(layout_mappings) $(variant_mappings)

0019-base.ml3_s.part: map-variants.py $(layout_mappings) $(variant_mappings)
	$(srcdir)/map-variants.py --want=mls --number=3 $@ $(layout_mappings) $(variant_mappings)

0021-base.ml4_s.part: map-variants.py $(layout_mappings) $(variant_mappings)
	$(srcdir)/map-variants.py --want=mls --number=4 $@ $(layout_mappings) $(variant_mappings)

0016-base.ml1v1_s.part: map-variants.py $(variant_mappings)
	$(srcdir)/map-variants.py --want=mlvs --number=1 $@ $(variant_mappings)

0023-base.ml2v2_s.part: map-variants.py $(variant_mappings)
	$(srcdir)/map-variants.py --want=mlvs --number=2 $@ $(variant_mappings)

0024-base.ml3v3_s.part: map-variants.py $(variant_mappings)
	$(srcdir)/map-variants.py --want=mlvs --number=3 $@ $(variant_mappings)

0025-base.ml4v4_s.part: map-variants.py $(variant_mappings)
	$(srcdir)/map-variants.py --want=mlvs --number=4 $@ $(variant_mappings)

0012-base.ml_s.part: map-variants.py $(layout_mappings) $(variant_mappings)
	$(srcdir)/map-variants.py --want=mls $@ $(layout_mappings) $(variant_mappings)

0010-base.mlv_s.part: map-variants.py $(layout_mappings) $(variant_mappings)
	$(srcdir)/map-variants.py --want=mlvs $@ $(variant_mappings)

EXTRA_DIST=0003-base.lists.part $(layout_mappings) $(variant_mappings) $(dist_parts) map-variants.py

CLEANFILES=$(scripts)
