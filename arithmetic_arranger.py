def arithmetic_arranger(problems, results = False):
  arranged_problems = str()
  line1 = ""
  line2 = ""
  dashes = ""
  line3 = ""
  ##check if problem list is more than 5
  if not len(problems) <= 5: 
    return ("Error: Too many problems.")
  else:
  # divide the list of problems into individual strings, one problem one string
    for problem in problems:
      components = problem.split()
      number1, operator, number2 = components[0], components[1], components[2]
      accepted_operators = ("+","-")
      #check if operator is accepted
      if operator not in accepted_operators:
        return ("Error: Operator must be \'+\' or \'-\'.")
      #check if numbers are digits
      elif not number1.isdigit() or not number2.isdigit():
        return ("Error: Numbers must only contain digits.")
      # check if max length of number is less than 4
      elif len(number1) > 4 or len(number2) > 4:
        return ("Error: Numbers cannot be more than four digits.")
      else:
        sum = None
        if operator == "+":
          sum = str(int(number1) + int(number2))
        elif operator == "-":
          sum = str(int(number1) - int(number2))

        max_len = max(str(number1), str(number2), key = len)
        ar_max_len = int(len(max_len)) + 2
        N1_aligned = str(number1).rjust(ar_max_len)
        N2_aligned = str(number2)
        sumx_aligned = str(sum).rjust(ar_max_len)
    
        if len(str(number2)) < len(str(number1)):
            N2_aligned = str(number2).rjust(int(len(max_len)))
    
        line = '-' * ar_max_len

        if problem != problems[-1]:
          line1 += N1_aligned + '    '
          line2 += operator + ' ' + N2_aligned + '    '
          dashes += line + '    '
          line3 += sumx_aligned + '    '
        else:
          line1 += N1_aligned 
          line2 += operator + ' ' + N2_aligned
          dashes += line 
          line3 += sumx_aligned
    arranged_problems = line1 + "\n" + line2 + "\n" + dashes
    if results == True:
      arranged_problems = line1 + "\n" + line2 + "\n" + dashes + "\n" + line3
  return (arranged_problems)
