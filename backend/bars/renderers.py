from core.renderers import CoreJSONRenderer


class BarJSONRenderer(CoreJSONRenderer):
    object_label = 'bar'
    pagination_object_label = 'bars'
    pagination_count_label = 'barsCount'
