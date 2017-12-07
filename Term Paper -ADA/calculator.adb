--
-- This is a calculator program made in ADA
-- for  my CIS343 class. 
--
with Text_IO;
with Gnat.Io; use Gnat.Io;
procedure Calculator is
	--This character will represent the action (+, -, /)
	operand: Character;

	--These intergers are the values to be used
	Val_One: Integer;
	Val_Two: Integer;

	--This integer will hold the result of the given calculation
	Result: Integer:= 0;
begin
	--Setting up a layout that prints first and once
	Put_Line("================================");
	New_line;
	Put_Line(" Welcome to the ADA Calculator");
	New_line;	
	Put_Line("================================");
	New_line;
	Put_Line(" This was made by Jamie Penzien");
	Put_Line("    for her CIS 343 class.");
	Put_Line("Perform calculation by entering");
	Put_Line("an operation 2+3, 4*2, 8/2 etc.");
	Put_Line("      Exit by typing 'qqq'.");
	Put_Line("             Enjoy!");
	New_line;
	Put_Line("================================");
	New_line;

	--Continuously asking for calculations
	loop
		New_line;
		Put_Line("Please enter a calculation: ");

		loop
			--This will take the first integer
			Get(Val_One);
			--The operation char
			Get(operand);
			--Then the second value
			Get(Val_Two);
			exit when operand /= ' ';
			if operand /= '/' AND Val_Two = 0 then 
				Put_Line("Cannot compute");
			end if;
		end loop;
		
		exit when operand = 'q' or operand = 'Q';
		
		--Get(Val_Two);
		
		--Text_IO.Skip_Line;
		
		--The operation to be performed given the operand's value
		case operand is
			when '=' 	=> Result := Val_One;
			when '+' 	=> Result := Val_One + Val_Two;
			when '-' 	=> Result := Val_One - Val_Two;
			when '*' 	=> Result := Val_One * Val_Two;
			--when '/' 	=> Result := Val_One / Val_Two;
			when '/' 	=>	if Val_Two = 0 then 
							Put_Line("Cannot divide by 0.");
						else
							Result := Val_one / Val_Two;
						end if;
			when '^' 	=> Result := Val_One ** Val_Two;
			when '0'..'9' 	=> Put_Line("Not an operation.");
			when others 	=> Put_Line("Not an operation.");
		end case;

		Put_Line("Your calculation results in: ");
		Put(Result);
	end loop;
end Calculator;

