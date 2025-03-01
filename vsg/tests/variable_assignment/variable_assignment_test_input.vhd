
architecture ARCH of ENTITY is

begin

  a := b;
   c := d;
  e := f;

  PROC_1 : process (a) is
  begin

    a(3 downto 0) := b;
  c := d;
    e := f;

    case CASE_LOGIC is
      when a = 1 =>

         a := b;
        c := d;
        e := f;

      when b = 1 =>

        a   :=  (b);
        c := d;
      e := f;

      when c = 1 =>

      --  a := b;
        c :=d;
        e := f;

      when others =>

        a:= b;
        c := d;
        e:= f;

    end case;

  end process PROC_1;

  a := b;
  c1 := d;
   e12 := f;

  PROC_2 : process (a) is
  begin

    a   := b or
            c or
          d = '1';
   c1  := d;
    e12 := f and g and h
           or i and j;

    case CASE_LOGIC is
      when a = 1 =>

        a := b;
        if a := 1 then
          c :=  d;
           e := f;
        end if;

      when b = 1 =>

        a := b;
        if a = 1 then
           c12 := d or e or
                   f and g;
          e1  := f and x or y;
        end if;

      when c = 1 =>

        a := b;
       c:= d;
        if a = 1 then
          e :=f;
        end if;

      when others =>

        a := b;
       c:= d;
         e := f;

        a := b or
           -- c := d or
           -- e := f or
             c;

    end case;

    a :=
         b;

  end process PROC_2;

  TEST_PROCESS : process

    procedure test_procedure (
      constant test1_c    : in boolean := true
     ) is
    begin
    end procedure test_procedure;

  begin

  end process TEST_PROCESS;

end architecture ARCH;
