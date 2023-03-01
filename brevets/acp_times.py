"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

#  br_km_hr is a dictionary with the number of hours a brevet would be if a rider
#  were to ride the minimum speed thoughout the entirety of the brevet 
br_km_hr = {200: 13.5, 300: 20, 400: 27, 600: 40, 1000: 75}


#br_speedOpt is a list of lists that contains the minimum and maximum speeds for each length of brevet 

br_speedOpt = [   (0, 200, 15, 34),
                  (200, 400, 15, 32),
                  (400, 600, 15, 30),
                  (600, 1000, 11.428, 28),
                  (1000, 1300, 13.333, 26)
                ]

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.




    Calculate:
     hours = ?brevet_start_time.shift(hours=hours, minutes=minutes)
     minutes = ?
    """

    print("This is the control dist: " + str(control_dist_km))
    print("THis is the brevet start time: " + str(brevet_start_time))

    total_time = 0


    if control_dist_km == 0:
       return brevet_start_time


    for i in br_speedOpt:
       min_d, max_d, min_s, max_s = i
       if control_dist_km >= min_d:
          #if control_dist_km <= max_d:
             if control_dist_km <= 200:
                tmp_time = control_dist_km / 34
                total_time += tmp_time
                break
             elif control_dist_km <= 400:
                tmp_time = (200/34) + ((control_dist_km - 200) / 32)
                total_time += tmp_time
                break
             elif control_dist_km <= 600:
                tmp_time = (200/34) + (200/32) + ((control_dist_km - 400) / 30)
                total_time += tmp_time
                break
             elif control_dist_km <= 1000:
                tmp_time = (200/34) + (200/32) + (200/30) + ((control_dist_km-600) / 28)
                total_time += tmp_time
                break

    hours = round(total_time)
    minutes = round((total_time - hours) * 60)

    return brevet_start_time.shift(hours=hours, minutes=minutes)
   

    """
    if control_dist_km >0 and control_dist_km <=200:
       min_d, max_d, min_s, max_s = br_speedOpt[0]
       tmp_time = control_dist_km / min_s
       total_time += tmp_time
       
    if control_dist_km >200 and control_dist_km <=400:
       min_d, max_d, min_s, max_s = br_speedOpt[1]
       min_d, max_d, min_s, max_s = br_speedOpt[0]
       tmp_time = control_dist_km / min_s
       total_time += tmp_time

    if control_dist_km >400 and control_dist_km <=600:
       min_d, max_d, min_s, max_s = br_speedOpt[2]
       min_d, max_d, min_s, max_s = br_speedOpt[0]
       tmp_time = control_dist_km / min_s
       total_time += tmp_time

    if control_dist_km > 600 and control_dist_km <=1000:
       min_d, max_d, min_s, max_s = br_speedOpt[3]
       min_d, max_d, min_s, max_s = br_speedOpt[0]
       tmp_time = control_dist_km / min_s
       total_time += tmp_time

    if control_dist_km >1000 and control_dist_km <=1300:
       min_d, max_d, min_s, max_s = br_speedOpt[4]
       min_d, max_d, min_s, max_s = br_speedOpt[0]
       tmp_time = control_dist_km / min_s
       total_time += tmp_time
         
    hours = int(total_time)
    minutes = round((total_time - hours) * 60)

    return brevet_start_time.shift(hours=hours, minutes=minutes) """


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object

       assert close_time(400, 400, arrow.get(``2001-08-14T06:35``)).format
       (``YYYY-MM-DDTHH:mm``) == arrow.get(``2001-08-15T09:35``).format(``YYYY-MM-DDTHH:mm``) 


    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    total = 0 

    if control_dist_km == 0:
       hours = 1
       total += hours
       return brevet_start_time.shift(hours=hours)

    elif control_dist_km > brevet_dist_km:
       add_dist = brevet_dist_km * 1.2
       print("here: ")
       print(add_dist)
       if control_dist_km <= add_dist:
          print(total)
          hours = int(total)
          minutes = round((total - hours) * 60)
          return brevet_start_time.shift(hours=hours, minutes=minutes)

    elif control_dist_km <= 60:
       time = (control_dist_km / 20) + 1
       total += time
    elif control_dist_km <= 600:
       time = control_dist_km / 15
       total += time
       if (control_dist_km == brevet_dist_km) and brevet_dist_km <=200:
          hours = int(total)
          minutes = round((total - hours) * 60) + 10
          return brevet_start_time.shift(hours=hours, minutes=minutes)
          
    elif control_dist_km <= 1000:
       first_km = 600 / 15
       remaining_km = (control_dist_km - 600) / 11.428
       time = first_km + remaining_km
       total += time


    hours = int(total)
    minutes = round((total - hours) * 60)

    return brevet_start_time.shift(hours=hours, minutes=minutes)
