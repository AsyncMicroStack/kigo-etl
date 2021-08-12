Kigo ETL framework
==============================================

.. image:: https://travis-ci.org/AsyncMicroStack/kigo-etl.svg?branch=master
   :target: http://travis-ci.org/AsyncMicroStack/kigo-etl

.. pull-quote ::
   Declarative ETL engine.

.. code-block:: python

   # helloworld.py

   from engine.mapping import bind_id


   @bind_id(object_id='input_1')
   class SomeClass:
      data_1 = '[31:43]'
      data_2 = '[49:61]'


Documentation
-------------

Documentation and links to additional resources are available at
https://www.asyncstack.org/kigo-etl


License
-------

Apache 2.0. See LICENSE for details.