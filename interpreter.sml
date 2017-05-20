datatype value = FUNCTION of value*command list* (value*value) list| INT of int| STR of string | NAME of string | BOOL of bool| BINDING of value*value| ERROR 

and command = push of value |pop| TRUE | FALSE |ERR| add|sub|mul|Div|rem|neg|swap|IF|AND|OR|NOTINMYHOUSE|EQUAL|LESSERTHAN|BIND|LET|END|FUNEND|CALL|RETURN|FUN of value*value| quit
	

	fun FunctionListz(x::xs, strings)= if x= #" " 
									   then (NAME(strings),NAME(implode xs)) 
									   else FunctionListz(xs, strings^Char.toString(x))

	fun reversemystack(x,y)= case x of [] => y
								| a::b => reversemystack(b, a::y)
	fun ReadMyFunction(input:string) =
		
		FunctionListz(explode (String.substring(input, 4, size(input)-5)), "")



	fun Closure(argument, commandlist,functionlist, map)= 
		(case commandlist of
			FUNEND::commandlist => (FUNCTION(argument, reversemystack(FUNEND::functionlist, []), map), commandlist)
			|a::b => Closure(argument,b, a::functionlist, map))



	fun FileReader(inStream:string, command)=
	if String.substring(inStream, 0, size(inStream)-1) = "or" then OR::command
	else if String.substring(inStream, 0, size(inStream)-1) = "if" then IF::command
	else if String.substring(inStream,0, 4) = "push" then
					if String.substring(inStream,5,1)= "\"" then 
						let
								val strCase= String.substring(inStream,5,size(inStream)-6)
						in
								push(STR(strCase))::command

						end



					else if valOf (Char.fromString(substring(inStream,5,1)))>= chr(97) andalso valOf (Char.fromString(substring(inStream,5,1)))<= chr(122) then
						let

								val nameCase = String.substring(inStream,5,size(inStream)-6)
						in 
								push(NAME(nameCase))::command
						end




		
					else if valOf (Char.fromString(substring(inStream,5,1)))>=chr(65) andalso valOf (Char.fromString(substring(inStream,5,1)))<=  chr(90) then
						let

								val nameCase = String.substring(inStream,5,size(inStream)-6)
						in 
								push(NAME(nameCase))::command
						end




					else if valOf (Char.fromString(substring(inStream,5,1)))>= chr(48)  andalso valOf (Char.fromString(substring(inStream,5,1)))<= chr(57) then
						let
								val intCase = valOf (Int.fromString(String.substring(inStream,5,size(inStream)-6)))
						in 		
								push(INT(intCase))::command
						end

			



	
					else if String.substring(inStream,5,1)= "-" then
	
						if List.all Char.isDigit (String.explode (String.substring(inStream, 6, size(inStream)-7))) then
			
						let
							val negintCase= valOf (Int.fromString("-" ^ String.substring(inStream, 6, size(inStream)-6)))
						in
							push(INT(negintCase))::command

						end
						
						else ERR::command

					else ERR::command
	else if String.substring(inStream, 0, size(inStream)-1) = "pop" then pop::command
	else if String.substring(inStream, 0, size(inStream)-1) = "and" then AND::command
	else if String.substring(inStream, 0, size(inStream)-1) = "add" then add::command
	else if String.substring(inStream, 0, size(inStream)-1) = "sub" then sub::command
	else if String.substring(inStream, 0, size(inStream)-1) = "mul" then mul::command
	else if String.substring(inStream, 0, size(inStream)-1) = "div" then Div::command
	else if String.substring(inStream, 0, size(inStream)-1) = "rem" then rem::command
	else if String.substring(inStream, 0, size(inStream)-1) = "let" then LET::command
	else if String.substring(inStream, 0, size(inStream)-1) = "end" then END::command
	else if String.substring(inStream, 0, size(inStream)-1) = "neg" then neg::command
	else if String.substring(inStream, 0, size(inStream)-1) = "not" then NOTINMYHOUSE::command
	else if String.substring(inStream, 0, size(inStream)-1) = "swap" then swap::command
	else if String.substring(inStream, 0, size(inStream)-1) = "bind" then BIND::command




	else if String.substring(inStream, 0, size(inStream)-1) = "call" then CALL::command
 	else if String.substring(inStream, 0, size(inStream)-1) = "funEnd" then FUNEND::command

	else if String.substring(inStream, 0, 3) = "fun" then  (print("HELLO");FUN(ReadMyFunction(inStream))::command)
	else if String.substring(inStream, 0, size(inStream)-1) = "return" then RETURN::command






	else if String.substring(inStream, 0, size(inStream)-1) = "quit" then quit::command 
	else if String.substring(inStream, 0, size(inStream)-1) = ":true:"  then TRUE::command
	else if String.substring(inStream, 0, size(inStream)-1) = ":false:" then FALSE::command	
	else if String.substring(inStream, 0, size(inStream)-1) = ":error:" then ERR::command
	else if String.substring(inStream, 0, size(inStream)-1) = "equal"   then EQUAL::command
	else if String.substring(inStream, 0, size(inStream)-1) = "lessThan" then LESSERTHAN::command
	else ERR::command

		
	fun printLine(INT(x)::xs) = if x < 0 
				    then "-"^Int.toString(~x)^"\n"^printLine(xs)
				    else Int.toString(x)^"\n"^printLine(xs) 
		|printLine(STR(x)::xs) = String.substring(x,1,String.size(x)-2)^"\n"^printLine(xs)
		|printLine(NAME(x)::xs) = x^"\n"^printLine(xs)
		|printLine(BOOL(x)::xs) = if Bool.toString(x)= "true"
								  then ":true:"^"\n"^printLine(xs)
								  else ":false:"^"\n"^printLine(xs)


		|printLine(BINDING(x)::xs)= ":unit:" ^ "\n" ^ printLine(xs)

		|printLine(ERROR::xs) = ":error:"^ "\n" ^ printLine(xs)
		|printLine([]) = ""


	
	fun first(a,_) = a
	fun second(_, b) = b


	fun MapLookUp(NAME(keys), []) = ERROR
		| MapLookUp(NAME(keys), []::z) = MapLookUp(NAME(keys), z)
		| MapLookUp(NAME(keys), (x::xs)::z) =if first(x)= NAME(keys)
				 			 			then second(x)
				 			 			else MapLookUp(NAME(keys),xs::z); 

	

(*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_*)

	fun interpret (push(stack)::t, x::z, map)= interpret( t , (stack::x)::z, map)
		

	
		| interpret(pop::t, (x::xs)::z, map) = interpret(t,xs::z, map)
			
	
		| interpret(add::t, (INT(x)::INT(y)::xs)::z, map)= interpret(t, (INT(x+y)::xs)::z, map)
		
		| interpret(add::t, (INT(x)::NAME(y)::xs)::z, map)= (case MapLookUp(NAME(y),map) of
															INT(A) => interpret(t, (INT(A+x)::xs)::z, map ) 
															| _ => interpret(t, (ERROR::INT(x)::NAME(y)::xs)::z, map))




		| interpret(add::t, (NAME(x)::INT(y)::xs)::z, map)= (case MapLookUp(NAME(x), map) of
															INT(A) => interpret(t, (INT(A+y)::xs)::z, map) 
															| _ => interpret(t, (ERROR::NAME(x)::INT(y)::xs)::z, map))
		| interpret(add::t, (NAME(x)::NAME(y)::xs)::z, map)= 
			(case (MapLookUp(NAME(y),map), MapLookUp(NAME(x), map)) of
				(INT(A), INT(B)) => interpret(t, (INT(A+B)::xs)::z, map)
				| _ => interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map))



		| interpret(sub::t, (INT(x)::INT(y)::xs)::z, map)= interpret(t, (INT(y-x)::xs)::z, map)

		| interpret(sub::t, (INT(x)::NAME(y)::xs)::z, map)= 
			(case MapLookUp(NAME(y),map) of
				INT(A) => interpret(t, (INT(A-x)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::INT(x)::NAME(y)::xs)::z, map))

		| interpret(sub::t, (NAME(x)::INT(y)::xs)::z, map)= 
			(case MapLookUp(NAME(x), map) of
				INT(A) => interpret(t, (INT(y-A)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::NAME(x)::INT(y)::xs)::z, map))

		| interpret(sub::t, (NAME(x)::NAME(y)::xs)::z, map)= 
			(case (MapLookUp(NAME(y),map), MapLookUp(NAME(x), map)) of
				(INT(A), INT(B)) => interpret(t, (INT(A-B)::xs)::z, map)
				| _ => interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map))
			
					  
		| interpret(mul::t,(INT(x)::INT(y)::xs)::z, map)= interpret(t, (INT(x*y)::xs)::z, map)
		
		| interpret(mul::t, (INT(x)::NAME(y)::xs)::z, map)= 
			(case MapLookUp(NAME(y),map) of
				INT(A) => interpret(t, (INT(A*x)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::INT(x)::NAME(y)::xs)::z, map))

		| interpret(mul::t, (NAME(x)::INT(y)::xs)::z, map)= 
			(case MapLookUp(NAME(x), map) of
				INT(A) => interpret(t, (INT(A*y)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::NAME(x)::INT(y)::xs)::z, map))

		| interpret(mul::t, (NAME(x)::NAME(y)::xs)::z, map)= 
			(case (MapLookUp(NAME(y),map), MapLookUp(NAME(x), map)) of
				(INT(A), INT(B)) => interpret(t, (INT(A*B)::xs)::z, map)
				| _ => interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map))
					  
		| interpret(Div::t,(INT(0)::NAME(y)::xs)::z, map)= interpret(t, (ERROR::INT(0)::NAME(y)::xs)::z, map)
		|interpret(Div::t, (INT(0)::INT(y)::xs)::z, map)= interpret(t , (ERROR::INT(0)::INT(y)::xs)::z, map)
			|interpret(Div::t, (INT(x)::INT(y)::xs)::z, map)=interpret ( t , (INT(y div x)::xs)::z, map)
			
		| interpret(Div::t, (INT(x)::NAME(y)::xs)::z, map)= 
			(case MapLookUp(NAME(y),map) of
				INT(A) => interpret(t, (INT(A div x)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::INT(x)::NAME(y)::xs)::z, map))

		| interpret(Div::t, (NAME(x)::INT(y)::xs)::z, map)= 
			(case MapLookUp(NAME(x), map) of
				INT(A) => if A= 0
						 then interpret(t , (ERROR::NAME(x)::INT(y)::xs)::z, map)

						 else interpret(t, (INT(y div A)::xs)::z, map ) 

				| _ => interpret(t, (ERROR::NAME(x)::INT(y)::xs)::z, map))


		| interpret(Div::t, (NAME(x)::NAME(y)::xs)::z, map)= 
			(case (MapLookUp(NAME(y),map), MapLookUp(NAME(x), map)) of
				(INT(A), INT(B)) => if A =0 
									then interpret(t , (ERROR::NAME(x)::NAME(y)::xs)::z, map)
									else interpret(t, (INT(B div A)::xs)::z, map)

				| _ => interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map))
				  

		| interpret(rem::t,(INT(0)::INT(y)::xs)::z, map)= interpret(t, (ERROR::INT(0)::INT(y)::xs)::z, map)
		| interpret(rem::t,(INT(0)::NAME(y)::xs)::z, map)= interpret(t, (ERROR::INT(0)::NAME(y)::xs)::z, map)

			|interpret(rem::t, (INT(x)::INT(y)::v)::z, map)= interpret(t, (INT(y mod x)::v)::z, map)
		
		| interpret(rem::t, (INT(x)::NAME(y)::xs)::z, map)= 
			(case MapLookUp(NAME(y),map) of
				INT(A) => interpret(t, (INT(A mod x)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::INT(x)::NAME(y)::xs)::z, map))

		| interpret(rem::t, (NAME(x)::INT(y)::xs)::z, map)= 
			(case MapLookUp(NAME(x), map) of
				INT(A) => if A= 0
						 then interpret(t , (ERROR::NAME(x)::INT(y)::xs)::z, map)

						 else interpret(t, (INT(y mod A)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::NAME(x)::INT(y)::xs)::z, map))

		| interpret(rem::t, (NAME(x)::NAME(y)::xs)::z, map)= 
			(case (MapLookUp(NAME(y),map), MapLookUp(NAME(x), map)) of
				(INT(A), INT(B)) => if A =0 
									then interpret(t , (ERROR::NAME(x)::NAME(y)::xs)::z, map)
									else interpret(t, (INT(B mod A)::xs)::z, map)
				| _ => interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map))


		|interpret (neg::t, (INT(x)::xs)::z, map) = interpret(t,(INT(~x)::xs)::z, map)
		| interpret(neg::t, (NAME(x)::xs)::z, map)= 
			(case MapLookUp(NAME(x),map) of
				INT(A) => interpret(t, (INT(~A)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::NAME(x)::xs)::z, map))

		
		| interpret(TRUE::t, xs::z, map) = interpret(t , (BOOL(true)::xs)::z, map)
	  		
	
		| interpret(FALSE::t, xs::z, map )= interpret( t , (BOOL(false)::xs)::z, map)
			

		| interpret (swap::t, (x::y::xs)::z, map ) = interpret( t , (y::x::xs)::z, map)


(*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-PART 2_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_*)

		| interpret (AND::t, (BOOL(x)::BOOL(y)::xs)::z, map ) = interpret( t, (BOOL(y andalso x)::xs)::z, map)
				| interpret(AND::t, (BOOL(x)::NAME(y)::xs)::z, map)= 
					(case MapLookUp(NAME(y),map) of
						BOOL(A) => interpret(t, (BOOL(A andalso x)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::BOOL(x)::NAME(y)::xs)::z, map))


				| interpret(AND::t, (NAME(x)::BOOL(y)::xs)::z, map)= 
					(case MapLookUp(NAME(x), map) of
						BOOL(A) => interpret(t, (BOOL(y andalso A)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::NAME(x)::BOOL(y)::xs)::z, map))
		

				| interpret(AND::t, (NAME(x)::NAME(y)::xs)::z, map)= 
					(case (MapLookUp(NAME(y),map), MapLookUp(NAME(x), map)) of
						(BOOL(A), BOOL(B)) => interpret(t, (BOOL(B andalso A)::xs)::z, map)
				| _ => interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map))



		| interpret (OR::t, (BOOL(x)::BOOL(y)::xs)::z, map) = interpret( t, (BOOL(y orelse x)::xs)::z, map)
				| interpret(OR::t, (BOOL(x)::NAME(y)::xs)::z, map)= 
					(case MapLookUp(NAME(y),map) of
						BOOL(A) => interpret(t, (BOOL(A orelse x)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::BOOL(x)::NAME(y)::xs)::z, map))


				| interpret(OR::t, (NAME(x)::BOOL(y)::xs)::z, map)= 
					(case MapLookUp(NAME(x), map) of
						BOOL(A) => interpret(t, (BOOL(y orelse A)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::NAME(x)::BOOL(y)::xs)::z, map))
		

				| interpret(OR::t, (NAME(x)::NAME(y)::xs)::z, map)= 
					(case (MapLookUp(NAME(y),map), MapLookUp(NAME(x), map)) of
						(BOOL(A), BOOL(B)) => interpret(t, (BOOL(B orelse A)::xs)::z, map)
				| _ => interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map))



		
		| interpret(NOTINMYHOUSE::t, (BOOL(x)::xs)::z, map) = interpret(t, (BOOL(not x)::xs)::z, map)
		| interpret(NOTINMYHOUSE::t, (NAME(x)::xs)::z, map)= 
					(case (MapLookUp(NAME(x),map)) of
						 BOOL(A) => interpret(t, (BOOL(not A)::xs)::z, map)
				| _ => interpret(t, (ERROR::NAME(x)::xs)::z, map))


		| interpret (EQUAL::t, (INT(x)::INT(y)::xs)::z, map)= interpret( t, (BOOL(y = x)::xs)::z, map)
				| interpret(EQUAL::t, (INT(x)::NAME(y)::xs)::z, map)= 
					(case MapLookUp(NAME(y),map) of
						INT(A) => interpret(t, (BOOL(A = x)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::INT(x)::NAME(y)::xs)::z, map))


				| interpret(EQUAL::t, (NAME(x)::INT(y)::xs)::z, map)= 
					(case MapLookUp(NAME(x), map) of
						INT(A) => interpret(t, (BOOL(y = A)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::NAME(x)::INT(y)::xs)::z, map))
		

				| interpret(EQUAL::t, (NAME(x)::NAME(y)::xs)::z, map)= 
					(case (MapLookUp(NAME(y),map), MapLookUp(NAME(x), map)) of
						(INT(A), INT(B)) => interpret(t, (BOOL(B = A)::xs)::z, map)
				| _ => interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map))

		| interpret (LESSERTHAN::t, (INT(x)::INT(y)::xs)::z, map)= interpret( t, (BOOL(y < x)::xs)::z, map)
				| interpret(LESSERTHAN::t, (INT(x)::NAME(y)::xs)::z, map)= 
					(case MapLookUp(NAME(y),map) of
						INT(A) => interpret(t, (BOOL(A < x)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::INT(x)::NAME(y)::xs)::z, map))


				| interpret(LESSERTHAN::t, (NAME(x)::INT(y)::xs)::z, map)= 
					(case MapLookUp(NAME(x), map) of
						INT(A) => interpret(t, (BOOL(y < A)::xs)::z, map ) 
				| _ => interpret(t, (ERROR::NAME(x)::INT(y)::xs)::z, map))
		

				| interpret(LESSERTHAN::t, (NAME(x)::NAME(y)::xs)::z, map)= 
					(case (MapLookUp(NAME(y),map), MapLookUp(NAME(x), map)) of
						(INT(A), INT(B)) => interpret(t, (BOOL(A < B)::xs)::z, map)
				| _ => interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map))


		| interpret(IF::t , (x::y::BOOL(true)::xs)::z, map)= interpret(t, (x::xs)::z, map)
		
		| interpret(IF::t , (x::y::BOOL(false)::xs)::z, map)= interpret(t, (y::xs)::z, map)
		| interpret(IF::t , (x::y::NAME(k)::xs)::z, map)= 
		(case (MapLookUp(NAME(k),map)) of
					BOOL(true) => interpret(t, (x::xs)::z, map)
				| BOOL(false)=> interpret(t, (y::xs)::z, map)
				| _ => interpret(t, (ERROR::x::y::NAME(k)::xs)::z, map))

(*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-BIND_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_*)




		| interpret (BIND::t, (ERROR::y)::z, maplist) = interpret (t, (ERROR::ERROR::y)::z, maplist)


	  	| interpret (BIND::t, (BINDING(x)::NAME(y)::xs)::z, map::maplist)=  interpret (t, ((BINDING(NAME(y),BINDING(x))::xs))::z,  ((NAME(y),BINDING(x))::map)::maplist)


		| interpret (BIND::t, (NAME(x)::NAME(y)::xs)::z, map::maplist) = if MapLookUp(NAME(x),map::maplist)= ERROR
															then interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map::maplist)
															else interpret(t, ((BINDING(MapLookUp(NAME(x),map::maplist), NAME(y))::xs))::z, (((NAME(y),MapLookUp(NAME(x),map::maplist)))::map)::maplist)


		| interpret (BIND::t, (INT(x)::NAME(y)::xs)::z, map::maplist)=  interpret (t, ((BINDING(NAME(y),INT(x)))::xs)::z,  ((NAME(y),INT(x))::map)::maplist )
			
		| interpret (BIND::t, (STR(x)::NAME(y)::xs)::z, map::maplist)=  interpret (t, ((BINDING(NAME(y),STR(x)))::xs)::z,  ((NAME(y),STR(x))::map)::maplist)
			
		| interpret (BIND::t, (BOOL(x)::NAME(y)::xs)::z, map::maplist)=  interpret (t, ((BINDING(NAME(y),BOOL(x)))::xs)::z,  ((NAME(y), BOOL(x))::map)::maplist)




(*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-END BIND-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_*)



		| interpret (LET::t, x, map)= interpret(t, []::x, []::map)

		| interpret (END::t, (a::x)::y::xs, map::maplist) = interpret (t, (a::y)::xs, maplist)  

(*______________________________________________FUNCTIONS!!!_____________________________________________________________*)

		| interpret (FUN(name,arg)::t, x::xs,  map::maplist) = 
			(case Closure(arg, t, [], map) of (FUNCTION(a),l) => interpret (l, (BINDING(name,FUNCTION(a))::x)::xs, ((name, FUNCTION(a))::map)::maplist))
		



		| interpret ( CALL::t, (NAME(x)::ERROR::xs)::z , map) = interpret(t, (ERROR::NAME(x)::ERROR::xs)::z, map)
		




		| interpret ( CALL::t, (NAME(x)::NAME(y)::xs)::z, map::maplist)= (case (MapLookUp(NAME(x),map::maplist), MapLookUp(NAME(y), map::maplist))of
																		 (FUNCTION(arg,instruction,mappp),ERROR) => interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map::maplist)
																		|(FUNCTION(arg,instruction,mappp),value)=> interpret(t, interpret(instruction, []::(xs::z), ((arg, value)::mappp)::(map::maplist))::z, map::maplist)
																		| _ => interpret(t, (ERROR::NAME(x)::NAME(y)::xs)::z, map::maplist))
	

		| interpret ( CALL::t, (NAME(x)::y::xs)::z,map::maplist) = (case MapLookUp(NAME(x), map::maplist) of 
																		FUNCTION(arg,instruction,mapl)=> interpret(t, interpret(instruction, []::(xs::z), ((arg, y)::mapl)::(map::maplist))::z, map::maplist)
																		| _ => interpret(t, (ERROR::NAME(x)::y::xs)::z, map::maplist))






		| interpret(FUNEND::t, x::xs::z, map)= xs



		| interpret(RETURN::t, (NAME(a)::x)::y::z, map)= (case (MapLookUp(NAME(a),map)) of 
															FUNCTION(u) => NAME(a)::y
															| u => u::y)

		| interpret(RETURN::t, (a::x)::y::z, map)= a::y
(*________________________________---------------END FUNCTION-----------____________________________________*)

		| interpret (quit::t, stackz::z, map) = stackz

		| interpret( [] , st::z, map ) = st

		| interpret(c::t ,st::z, map)= interpret(t , (ERROR::st)::z, map)




	fun interpreter(inFile:string,outFile: string) =
	let
		val inStream = TextIO.openIn inFile
		val outStream = TextIO.openOut outFile 
		val readLine = TextIO.inputLine inStream 

	fun helper(readLine : string option, stack) =
		case readLine of
		        NONE => (TextIO.output(outStream, printLine(interpret(stack, []::[], []::[]))); TextIO.closeOut outStream)
			| SOME(c) => ((FileReader(c, stack));
			helper(TextIO.inputLine inStream, stack@FileReader(c, [])));
		in 
			helper(readLine,[])
		end

