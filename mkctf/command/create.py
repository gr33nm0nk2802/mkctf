'''
file: create.py
date: 2018-02-27
author: koromodako
purpose:

'''
# =============================================================================
#  FUNCTIONS
# =============================================================================
async def create(args, repo):
    '''Creates a challenge
    '''
    status = repo.create_chall(args.configuration)
    return {'status': status} if args.json else status

