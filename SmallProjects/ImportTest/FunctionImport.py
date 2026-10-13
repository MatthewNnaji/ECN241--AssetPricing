"Importing functions from other files"
from Adding import arithmetic as summation #renames the function to summation; to call the function say summation() instead of arithmetic()
print(summation(2,3))

import Multiplication as mult #renames the whole file to mult - if you reference the file it must now be with 'mult'
print(mult.exponentiation(2,3))


"import SmallProjects.ImportTest.Multiplication as Multiplication" #this is how you would import in a real project (from different directories)