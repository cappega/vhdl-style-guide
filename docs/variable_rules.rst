Variable Rules
--------------

variable_001
############

This rule checks the indent of variable declarations.

**Violation**

.. code-block:: vhdl

   PROC : process () is

   variable count : integer;
         variable counter : integer;

   begin

**Fix**

.. code-block:: vhdl

   PROC : process () is

     variable count : integer;
     variable counter : integer;

   begin

variable_002
############

This rule checks the **variable** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   VARIABLE count : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_003
############

This rule checks for a single space after the **variable** keyword.

**Violation**

.. code-block:: vhdl

   variable     count : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_004
############

This rule checks the variable name is lowercase.

**Violation**

.. code-block:: vhdl

   variable COUNT : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_005
############

This rule checks there is a single space after the colon.

**Violation**

.. code-block:: vhdl

   variable count   :integer;
   variable counter :     integer;

**Fix**

.. code-block:: vhdl

   variable count   : integer;
   variable counter : integer;

variable_006
############

This rule checks for at least a single space before the colon.

**Violation**

.. code-block:: vhdl

   variable count: integer;
   variable counter : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;
   variable counter : integer;

variable_007
############

This rule checks for default assignments in variable declarations.

**Violation**

.. code-block:: vhdl

   variable count : integer := 32;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_009
############

This rule checks the alignment of colons over multiple lines in the architecture declarative region.

**Violation**

.. code-block:: vhdl

   architecture ARCH of ENTITY1 is

     variable count : integer;
     variable counter : integer;

   begin

**Fix**

.. code-block:: vhdl

   architecture ARCH of ENTITY1 is

     variable count   : integer;
     variable counter : integer;

   begin

variable_010
############

This rule checks the variable type is lowercase.

**Violation**

.. code-block:: vhdl

   variable count : INTEGER;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_011
############

This rule checks for consistent capitalization of variable names.

**Violation**

.. code-block:: vhdl

   architecture RTL of ENTITY1 is

     shared variable var1 : std_logic;
     shared variable var2 : std_logic;

   begin

     PROC_NAME : process () is

       variable var3 : std_logic;
       variable var4 : std_logic;

     begin

       Var1 <= '0';

       if (VAR2 = '0') then
         vaR3 <= '1';
       elisif (var2 = '1') then
         VAR4 <= '0';
       end if;

     end process PROC_NAME;

   end architecture RTL;

**Fix**

.. code-block:: vhdl

   PROC_NAME : process () is

     variable var1 : std_logic;
     variable var2 : std_logic;
     variable var3 : std_logic;
     variable var4 : std_logic;

   begin

     var1 <= '0';

     if (var2 = '0') then
       var3 <= '1';
     elisif (var2 = '1') then
       var4 <= '0';
     end if;

   end process PROC_NAME;

