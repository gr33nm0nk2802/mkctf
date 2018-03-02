# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     file: init.py
#     date: 2018-02-27
#   author: paul.dautry
#  purpose:
#
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# =============================================================================
#  IMPORTS
# =============================================================================
# =============================================================================
#  FUNCTIONS
# =============================================================================
##
## @brief      { function_description }
##
## @param      args         The arguments
## @param      glob_conf    The global conf
## @param      logger       The logger
##
def init(args, repo, logger):
    if repo.get_conf() is None:
        repo.init()
        logger.info("mkctf repository created.")
        repo.print_conf()
        return True

    logger.info("already a mkctf repository.")
    return False

