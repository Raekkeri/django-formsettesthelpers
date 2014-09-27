"""
Formset test helpers for Django.

Author: Teemu Husso (teemu.husso@gmail.com)
"""


__all__ = ['ModelFormsetHelper']


class ModelFormsetHelper(object):
    def __init__(self, formset_class):
        self.formset = formset_class()
        self.fields = self.formset[0].fields.keys()
        self.prefix = self.formset.prefix

    def generate(self, data, **kwargs):
        ret = {}
        index = 0
        default_values = self.default_values()
        for form_data in data:
            form_prefix = self.single_form_prefix(index)
            form_data = (self._to_dict(form_data) if isinstance(form_data, list)
                    else form_data)
            d = default_values.copy()
            d.update(form_data)
            for key, value in d.iteritems():
                ret['%s%s' % (form_prefix, key)] = value
            index += 1
        ret.update(self.generate_managementform_data(ret, **kwargs))
        return ret

    def single_form_prefix(self, index):
        return '%s-%d-' % (self.prefix, index)

    def _to_dict(self, li):
        raise NotImplementedError

    def generate_managementform_data(self, *args, **kwargs):
        max_num_forms = kwargs.get('max_num_forms', 1000)
        min_num_forms = kwargs.get('min_num_forms', 0)
        total_forms = kwargs.get('total_forms', 3)
        initial_forms = kwargs.get('initial_forms', 0)
        d = ((u'MAX_NUM_FORMS', max_num_forms),
                (u'MIN_NUM_FORMS', min_num_forms),
                (u'INITIAL_FORMS', initial_forms),
                (u'TOTAL_FORMS', total_forms))
        return dict(('%s-%s' % (self.prefix, i[0]), i[1]) for i in d)

    def default_values(self):
        ret = {}
        instance = self.formset[0].instance
        for field in self.fields:
            if hasattr(instance, field):
                ret[field] = getattr(instance, field)
                if ret[field] == None:
                    ret[field] = ''
        return ret