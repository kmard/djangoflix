
from playlists.models import Playlist
from videos.models import Video

# python manage.py shell

video_a = Video.objects.create(title = 'My title',video_id = 'abc12')
playlist_a = Playlist.objects.create(title="This is my title",video = self.video_a)

# >>> dir(video_a)
# ['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_cons
# traints', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '
# _check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_inse
# rt', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_
# prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_state', 'active', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'description', 'from_db', 'full_clean', 'get_deferred_fields', '
# get_playlist_ids', 'get_state_display', 'id', 'objects', 'pk', 'playlist_set', 'prepare_database_save', 'publish_timestamp', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'slug', 'state', 'timestamp', 'title', 'uniq
# ue_error_message', 'updated', 'validate_unique', 'video_id']
