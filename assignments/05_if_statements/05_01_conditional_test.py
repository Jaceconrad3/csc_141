# Jace Conrad
# Chapter 5
# These are if/then statements representing attributes of curry and lebron
# It uses greater than signs to compare and when the attribute in front is greater it will print
# the statement

# Stephen Curry attributes
stephen_curry_three_point = 99
stephen_curry_dunk = 65
stephen_curry_ball_handle = 96
stephen_curry_layup = 92
stephen_curry_strength = 68

# Lebron James attributes
lebron_james_three_point = 85
lebron_james_dunk = 99
lebron_james_ball_handle = 88
lebron_james_layup = 97
lebron_james_strength = 95


# First 5 are true

if stephen_curry_three_point > lebron_james_three_point:
    print("\nCurry is a better shooter than Lebron")

if lebron_james_dunk > stephen_curry_dunk: 
    print("\nLebron can slam dunk that ball way better than curry")

if stephen_curry_ball_handle > lebron_james_ball_handle:
    print("\nCurry got that ball on a string! Lebron ain't close!")

if lebron_james_layup > stephen_curry_layup: 
    print("\nLebrons layup is slightly better than currys")

if lebron_james_strength > stephen_curry_strength:
    print("\nLebron is way stronger and physical than curry")


# Last 5 are false

if lebron_james_three_point > stephen_curry_three_point:
    print("\nLebron is a way better shooter")

if stephen_curry_dunk > lebron_james_dunk:
    print("\nCurry can dunk way better than LBJ")

if lebron_james_ball_handle > stephen_curry_ball_handle:
    print("\nLBJ got it on a string compared to curry")

if stephen_curry_layup > lebron_james_layup:
    print("\ncurry can lay it better than LBJ")

if stephen_curry_strength > lebron_james_strength:
    print("\nCurry is more ocky than lebron!")