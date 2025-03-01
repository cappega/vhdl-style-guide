For Loop Rules
--------------

for_loop_001
############

This rule checks the indentation of the **for** keyword.

**Violation**

.. code-block:: vhdl

   FIFO_PROC : process () is
   begin

   for index in 4 to 23 loop

     end loop;

   end process;

**Fix**

.. code-block:: vhdl

   FIFO_PROC : process () is
   begin

     for index in 4 to 23 loop

     end loop;

   end process;

for_loop_002
############

This rule checks the indentation of the **end loop** keywords.

**Violation**

.. code-block:: vhdl

   FIFO_PROC : process () is
   begin

     for index in 4 to 23 loop

        end loop;

   end process;

**Fix**

.. code-block:: vhdl

   FIFO_PROC : process () is
   begin

     for index in 4 to 23 loop

     end loop;

   end process;

for_loop_003
############

This rule checks if a label on a for loop is uppercase.

**Violation**

.. code-block:: vhdl

     label : for index in 4 to 23 loop
     Label : for index in 0 to 100 loop

**Fix**

.. code-block:: vhdl

     LABEL : for index in 4 to 23 loop
     LABEL : for index in 0 to 100 loop

for_loop_004
############

This rule checks if a label exists on a for loop that a single space exists between the label and the :. 

**Violation**

.. code-block:: vhdl

     LABEL: for index in 4 to 23 loop
     LABEL    : for index in 0 to 100 loop

**Fix**

.. code-block:: vhdl

     LABEL : for index in 4 to 23 loop
     LABEL : for index in 0 to 100 loop

for_loop_005
############

This rule checks if a label exists on a for loop that a single space exists after the :. 

**Violation**

.. code-block:: vhdl

     LABEL :    for index in 4 to 23 loop
     LABEL :  for index in 0 to 100 loop

**Fix**

.. code-block:: vhdl

     LABEL : for index in 4 to 23 loop
     LABEL : for index in 0 to 100 loop
