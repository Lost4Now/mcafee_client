Setup
=====

A wrapper around the ePO API.
Simply treat the client object as a callable function, passing the command name and parameters.

Install::

    $ pip install mcafee-client

Use::

    from mcafee_epo import McClient
    mc = McClient('https://localhost:8443', 'user', 'password')
    systems = mc('system.find', '')