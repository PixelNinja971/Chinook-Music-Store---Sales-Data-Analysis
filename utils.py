REQUETE_TOP_VENTES = """
SELECT track.Name, sum(invoiceline.Quantity) AS total_ventes
FROM track
INNER JOIN invoiceline ON track.trackId = invoiceline.trackId
GROUP BY track.Name
ORDER BY total_ventes DESC
LIMIT 10
"""

REQUETE_PAYS = """
Select BILLINGCOUNTRY,SUM(TOTAL) as total FROM INVOICE
GROUP BY billingcountry 
Order by total desc
Limit 10
"""

REQUETE_EMPLOYEE = """
SELECT employee.FirstName, employee.LastName ,sum(invoice.total) as total_des_ventes_employer
FROM employee
INNER JOIN customer ON employee.EmployeeId = customer.supportRepId
INNER JOIN invoice ON customer.CustomerId = invoice.CustomerID
Group by employee.EmployeeId
"""
