from Products.CMFCore.utils import getToolByName
from collective.portlet.mybookmarks import logger

default_profile = 'profile-collective.portlet.mybookmarks:default'


def upgrade(upgrade_product, version):
    """ Decorator for updating the QuickInstaller of a upgrade """
    def wrap_func(fn):
        def wrap_func_args(context, *args):
            p = getToolByName(context, 'portal_quickinstaller').get(upgrade_product)
            setattr(p, 'installedversion', version)
            return fn(context, *args)
        return wrap_func_args
    return wrap_func


@upgrade('collective.portlet.mybookmarks', '1.2.0')
def to_1(context):
    """
    Upgrades to 1.2.0 version: add default bookmarks configuration
    """
    logger.info('Upgrading collective.portlet.mybookmarks to version 1')
    context.runImportStepFromProfile('profile-collective.portlet.mybookmarks:default', 'mybookmarks.importvarious')
    logger.info('Reinstalled My Bookmark Portlet')
