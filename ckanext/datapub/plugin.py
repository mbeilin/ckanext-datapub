import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from . import helpers


class DatapubPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'datapub')

    # ITemplateHelpers

    def get_helpers(self):
        return {
                'extstorage_lfs_url': helpers.lfs_url,
                'extstorage_organization_name': helpers.organization_name}
