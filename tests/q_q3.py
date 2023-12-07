test = {
  'name': 'Question q3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'q3'
          >>> 'q3' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'q3'
          >>> # from its initial state (of ...)
          >>> q3 is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # a + 5 * b is the whole expression, and not a sub-expression.
          >>> q3 == 3
          False
          """,
          'hidden': False,
          'locked': False
        },

      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
