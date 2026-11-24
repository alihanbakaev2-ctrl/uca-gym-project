"""One-shot writer for exercises.json. Not imported by the app."""
import json
from pathlib import Path

def slug(name):
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in name).strip("-").replace("--", "-")

def group(primary, rows):
    items = []
    for name, secondary, equipment, difficulty, cues in rows:
        items.append({
            "id": slug(name),
            "name": name,
            "primary": primary,
            "secondary": secondary,
            "equipment": equipment,
            "difficulty": difficulty,
            "cues": cues,
        })
    return items

C = "Chest"
B = "Back"
S = "Shoulders"
BI = "Biceps"
T = "Triceps"
F = "Forearms"
Q = "Quads"
H = "Hamstrings"
G = "Glutes"
CA = "Calves"
A = "Abs/Core"

data = []
data += group("Chest", [
    ("Barbell Bench Press", [S, T], "Barbell", "Intermediate", ["Plant your feet and pinch the shoulder blades.", "Lower the bar to the mid-chest.", "Press up without bouncing.", "Keep the wrists stacked over the elbows."]),
    ("Incline Barbell Press", [S, T], "Barbell", "Intermediate", ["Set the bench around 30 degrees.", "Touch the bar high on the chest.", "Drive the bar back over the shoulders."]),
    ("Decline Barbell Press", [T], "Barbell", "Intermediate", ["Hook the feet and keep the hips down.", "Lower to the lower chest.", "Press without flaring the elbows wide."]),
    ("Dumbbell Bench Press", [S, T], "Dumbbell", "Beginner", ["Start with the bells over the chest.", "Lower until the elbows are just below the bench.", "Press the bells up and slightly inward."]),
    ("Incline Dumbbell Press", [S, T], "Dumbbell", "Beginner", ["Keep the bench at a modest incline.", "Lower the bells beside the upper chest.", "Press until the arms are long, not locked hard."]),
    ("Dumbbell Fly", [S], "Dumbbell", "Intermediate", ["Soft bend in the elbows stays fixed.", "Open only until the chest stretches.", "Sweep the bells back together over the chest."]),
    ("Incline Dumbbell Fly", [S], "Dumbbell", "Intermediate", ["Lie on a low incline.", "Open the arms with a soft elbow.", "Squeeze the chest as the bells meet."]),
    ("Cable Crossover", [S], "Cable", "Intermediate", ["Step forward so the cables stay loaded.", "Bring the hands together in front of the chest.", "Control the return."]),
    ("Low Cable Fly", [S], "Cable", "Intermediate", ["Set the pulleys low.", "Arc the handles up toward the chest.", "Stop before the shoulders shrug."]),
    ("Pec Deck", [S], "Machine", "Beginner", ["Match the seat so the elbows stay at chest height.", "Squeeze until the arms are in front of you.", "Do not let the stack slam."]),
    ("Machine Chest Press", [S, T], "Machine", "Beginner", ["Set the seat so the handles start at chest height.", "Press until the elbows are almost straight.", "Return under control."]),
    ("Push-Up", [S, T], "Bodyweight", "Beginner", ["Hands under the shoulders.", "Body stays one straight line.", "Chest travels to the floor, then press away."]),
    ("Diamond Push-Up", [T], "Bodyweight", "Intermediate", ["Hands form a diamond under the chest.", "Elbows track back, not straight out.", "Keep the hips from sagging."]),
    ("Chest Dip", [T, S], "Bodyweight", "Advanced", ["Lean the torso slightly forward.", "Lower until the shoulders are near the elbows.", "Press up without shrugging."]),
    ("Landmine Press", [S, T], "Barbell", "Intermediate", ["Stagger the stance and brace.", "Press the bar up and slightly in.", "Don't overarch the lower back."]),
])
data += group("Back", [
    ("Conventional Deadlift", [G, H], "Barbell", "Advanced", ["Bar starts over the mid-foot.", "Brace, then push the floor away.", "Keep the bar touching the legs.", "Stand tall without leaning back."]),
    ("Barbell Bent-Over Row", [BI], "Barbell", "Intermediate", ["Hinge until the torso is near parallel.", "Pull the bar to the lower ribs.", "Lower it without rounding the back."]),
    ("Pendlay Row", [BI], "Barbell", "Advanced", ["Reset the bar on the floor each rep.", "Torso stays parallel.", "Pull explosively to the belly."]),
    ("Single-Arm Dumbbell Row", [BI], "Dumbbell", "Beginner", ["Brace the free hand on a bench.", "Pull the bell to the hip.", "Don't twist the shoulders open."]),
    ("Chest-Supported Row", [BI], "Dumbbell", "Beginner", ["Lie on an incline bench.", "Pull the bells toward the hips.", "Pause at the top without shrugging."]),
    ("Lat Pulldown", [BI], "Cable", "Beginner", ["Grip just outside the shoulders.", "Pull the bar to the upper chest.", "Let the shoulders rise on the way up."]),
    ("Wide-Grip Lat Pulldown", [BI], "Cable", "Intermediate", ["Take a wide grip.", "Lead with the elbows down and out.", "Stop at the collarbone."]),
    ("Pull-Up", [BI], "Bodyweight", "Intermediate", ["Start from a dead hang.", "Pull the chest toward the bar.", "Lower until the arms are straight."]),
    ("Chin-Up", [BI], "Bodyweight", "Intermediate", ["Palms face you.", "Pull until the chin clears the bar.", "Lower without swinging."]),
    ("Seated Cable Row", [BI], "Cable", "Beginner", ["Sit tall with a soft knee bend.", "Pull the handle to the ribs.", "Reach forward without collapsing."]),
    ("Straight-Arm Pulldown", [], "Cable", "Intermediate", ["Arms stay nearly straight.", "Pull the bar down to the thighs.", "Feel the lats, not a shrug."]),
    ("T-Bar Row", [BI], "Barbell", "Intermediate", ["Hinge and brace.", "Pull the handle into the stomach.", "Control the lowering."]),
    ("Meadows Row", [BI], "Barbell", "Advanced", ["Stand beside the landmine.", "Row the end of the bar to the hip.", "Keep the chest proud."]),
    ("Inverted Row", [BI], "Bodyweight", "Beginner", ["Body is a straight line under the bar.", "Pull the chest to the bar.", "Lower until the arms are long."]),
    ("Rack Pull", [G, H], "Barbell", "Intermediate", ["Bar starts just below the knee.", "Brace and stand tall.", "Don't lean back at the top."]),
])
data += group("Shoulders", [
    ("Overhead Press", [T], "Barbell", "Intermediate", ["Squeeze the glutes and brace.", "Bar starts on the front of the shoulders.", "Press it to finish over the mid-foot.", "Head comes through at the top."]),
    ("Seated Dumbbell Press", [T], "Dumbbell", "Beginner", ["Sit tall against the bench.", "Press the bells overhead.", "Lower to ear level."]),
    ("Arnold Press", [T], "Dumbbell", "Intermediate", ["Start with palms facing you.", "Rotate the palms out as you press.", "Reverse the path on the way down."]),
    ("Dumbbell Lateral Raise", [], "Dumbbell", "Beginner", ["Soft elbows.", "Raise to shoulder height.", "Lead with the elbows, not the hands."]),
    ("Cable Lateral Raise", [], "Cable", "Intermediate", ["Stand side-on to the stack.", "Raise the arm out to shoulder height.", "Don't shrug the trap."]),
    ("Dumbbell Front Raise", ["Chest"], "Dumbbell", "Beginner", ["Raise one or both bells to eye level.", "Keep a soft elbow.", "Lower slowly."]),
    ("Rear Delt Fly", ["Back"], "Dumbbell", "Beginner", ["Hinge until the chest faces the floor.", "Open the arms wide.", "Squeeze the shoulder blades lightly."]),
    ("Face Pull", ["Back"], "Cable", "Beginner", ["Set the rope at face height.", "Pull toward the nose and finish hands wide.", "Pause with the shoulders externally rotated."]),
    ("Upright Row", ["Back"], "Barbell", "Intermediate", ["Take a shoulder-width grip.", "Pull the bar to the lower chest.", "Stop if the shoulders pinch."]),
    ("Machine Shoulder Press", [T], "Machine", "Beginner", ["Handles start near the shoulders.", "Press up without locking hard.", "Control the return."]),
    ("Push Press", [T, Q], "Barbell", "Advanced", ["Dip the knees a few inches.", "Drive the bar overhead with the legs.", "Lock out over the mid-foot."]),
    ("Bradford Press", [T], "Barbell", "Advanced", ["Press just over the head.", "Lower it behind, then back in front.", "Use a modest weight."]),
    ("Cable Rear Delt Fly", ["Back"], "Cable", "Intermediate", ["Cross the cables in front.", "Open the arms to the sides.", "Keep the chest down."]),
    ("Dumbbell Shrug", ["Back"], "Dumbbell", "Beginner", ["Bells hang at the sides.", "Shrug straight up.", "Lower all the way."]),
    ("Barbell Shrug", ["Back"], "Barbell", "Beginner", ["Hold the bar at the thighs.", "Shrug up and slightly back.", "Don't roll the shoulders."]),
])
data += group("Biceps", [
    ("Barbell Curl", [F], "Barbell", "Beginner", ["Elbows stay near the ribs.", "Curl without swinging the hips.", "Lower until the arms are straight."]),
    ("EZ-Bar Curl", [F], "Barbell", "Beginner", ["Use the angled grips.", "Keep the wrists neutral.", "Squeeze at the top without leaning back."]),
    ("Dumbbell Curl", [F], "Dumbbell", "Beginner", ["Alternate or curl together.", "Supinate the palm as you lift.", "Don't rock the torso."]),
    ("Hammer Curl", [F], "Dumbbell", "Beginner", ["Palms face each other.", "Curl to the shoulder.", "Keep the elbows still."]),
    ("Incline Dumbbell Curl", [F], "Dumbbell", "Intermediate", ["Lie on an incline so the arms hang back.", "Curl without moving the upper arm.", "Feel the stretch at the bottom."]),
    ("Preacher Curl", [F], "Barbell", "Intermediate", ["Upper arms stay on the pad.", "Lower until the elbow is nearly straight.", "Don't bounce out of the bottom."]),
    ("Concentration Curl", [], "Dumbbell", "Beginner", ["Brace the elbow on the inner thigh.", "Curl the bell to the shoulder.", "Lower slowly."]),
    ("Cable Curl", [F], "Cable", "Beginner", ["Stand close to the stack.", "Curl the bar without letting the elbows drift.", "Control the eccentric."]),
    ("Bayesian Cable Curl", [], "Cable", "Intermediate", ["Face away from the stack.", "Arm is slightly behind the body.", "Curl without swinging."]),
    ("Spider Curl", [], "Dumbbell", "Intermediate", ["Chest on an incline bench.", "Upper arms hang straight down.", "Curl and pause at the top."]),
    ("Reverse Curl", [F], "Barbell", "Intermediate", ["Palms face down.", "Curl with the elbows pinned.", "Keep the wrists straight."]),
    ("Zottman Curl", [F], "Dumbbell", "Intermediate", ["Curl with palms up.", "Rotate palms down at the top.", "Lower slowly in that grip."]),
    ("Cable Rope Hammer Curl", [F], "Cable", "Beginner", ["Thumbs point up.", "Curl the rope toward the ears.", "Squeeze and lower."]),
    ("Machine Preacher Curl", [], "Machine", "Beginner", ["Set the seat so the armpits meet the pad.", "Curl without lifting the elbows.", "Lower under control."]),
    ("Waiter Curl", [F], "Dumbbell", "Intermediate", ["Hold one bell with both hands under the plate.", "Curl it like a tray.", "Keep the elbows forward."]),
])
data += group("Triceps", [
    ("Close-Grip Bench Press", ["Chest"], "Barbell", "Intermediate", ["Hands just inside shoulder width.", "Elbows stay closer to the ribs.", "Touch the lower chest and press."]),
    ("Skull Crusher", [], "Barbell", "Intermediate", ["Upper arms stay vertical.", "Bend only at the elbows.", "Lower toward the forehead, then extend."]),
    ("Overhead Dumbbell Extension", [], "Dumbbell", "Beginner", ["Hold one bell overhead.", "Lower it behind the head.", "Extend without flaring the ribs."]),
    ("Cable Pushdown", [], "Cable", "Beginner", ["Pin the elbows to the sides.", "Straighten the arms.", "Don't let the shoulders roll forward."]),
    ("Rope Pushdown", [], "Cable", "Beginner", ["Split the rope at the bottom.", "Elbows stay still.", "Control the return to the chest."]),
    ("Overhead Cable Extension", [], "Cable", "Intermediate", ["Face away and reach overhead.", "Bend the elbows behind the head.", "Extend to a long arm."]),
    ("Parallel Bar Dip", ["Chest"], "Bodyweight", "Intermediate", ["Stay more upright for triceps.", "Lower until the elbows are near 90 degrees.", "Press up to a tall lockout."]),
    ("Bench Dip", ["Chest"], "Bodyweight", "Beginner", ["Hands on a bench behind you.", "Lower the hips by bending the elbows.", "Don't let the shoulders dump forward."]),
    ("Dumbbell Kickback", [], "Dumbbell", "Beginner", ["Hinge and pin the upper arm.", "Extend the forearm back.", "Squeeze at the straight arm."]),
    ("JM Press", ["Chest"], "Barbell", "Advanced", ["Lower the bar toward the chin and upper chest.", "Elbows drift forward.", "Press back to lockout."]),
    ("Tate Press", [], "Dumbbell", "Advanced", ["Bells start over the chest, palms forward.", "Bend the elbows out and down.", "Extend back up."]),
    ("Single-Arm Cable Pushdown", [], "Cable", "Beginner", ["One hand on the handle.", "Elbow glued to the side.", "Extend and pause."]),
    ("French Press", [], "Barbell", "Intermediate", ["Lie down and start with the bar over the shoulders.", "Lower behind the head.", "Extend back over the shoulders."]),
    ("Machine Dip", ["Chest"], "Machine", "Beginner", ["Set the seat so the hands start near the shoulders.", "Press down until the arms are straight.", "Return slowly."]),
    ("Reverse-Grip Pushdown", [], "Cable", "Intermediate", ["Palms face up.", "Elbows stay pinned.", "Press the bar down and squeeze."]),
])
data += group("Forearms", [
    ("Wrist Curl", [], "Barbell", "Beginner", ["Forearms rest on the thighs.", "Curl the wrists up.", "Lower until the fingers open slightly."]),
    ("Reverse Wrist Curl", [], "Barbell", "Beginner", ["Palms face down.", "Lift the back of the hand.", "Use a light bar."]),
    ("Farmer Carry", [A], "Dumbbell", "Beginner", ["Stand tall with heavy bells.", "Walk in short, even steps.", "Don't lean to one side."]),
    ("Behind-the-Back Wrist Curl", [], "Barbell", "Intermediate", ["Hold the bar behind the thighs.", "Curl the wrists up.", "Keep the arms straight."]),
    ("Plate Pinch", [], "Other", "Intermediate", ["Pinch two plates smooth-side out.", "Hold for time.", "Stand tall."]),
    ("Towel Hang", ["Back"], "Bodyweight", "Intermediate", ["Hang from a towel over a bar.", "Keep the shoulders active.", "Hold until the grip fades."]),
    ("Dead Hang", ["Back"], "Bodyweight", "Beginner", ["Hang from a bar with a full grip.", "Ribs down, legs quiet.", "Breathe and hold."]),
    ("Finger Curl", [], "Barbell", "Beginner", ["Let the bar roll to the fingers.", "Curl it back into the palm.", "Keep the forearms supported."]),
    ("Barbell Hold", [], "Barbell", "Intermediate", ["Hold a heavy bar at the thighs.", "Stand tall.", "Time the hold."]),
    ("Dumbbell Pronation", [], "Dumbbell", "Beginner", ["Hold the bell at one end.", "Rotate the palm down and up.", "Move only the forearm."]),
    ("Wrist Roller", [], "Other", "Intermediate", ["Roll the rope up with the wrists.", "Reverse it down slowly.", "Arms stay in front of you."]),
    ("Thick-Bar Hold", [], "Barbell", "Advanced", ["Grip a thick handle.", "Hold at the sides or in front.", "Stop before the grip opens."]),
    ("Reverse-Grip Cable Curl", [BI], "Cable", "Intermediate", ["Palms down on the bar.", "Curl without swinging.", "This loads the forearm and brachialis."]),
    ("Radial Deviation", [], "Dumbbell", "Beginner", ["Hold the bell like a hammer, thumb up.", "Tilt the wrist toward the thumb.", "Small range, light weight."]),
    ("Suitcase Carry", [A], "Dumbbell", "Beginner", ["Carry one bell at the side.", "Don't lean away from it.", "Switch sides."]),
])
data += group("Quads", [
    ("Back Squat", [G], "Barbell", "Intermediate", ["Bar on the upper back.", "Sit down and slightly back.", "Knees track over the toes.", "Stand tall to finish."]),
    ("Front Squat", [A], "Barbell", "Advanced", ["Elbows stay high.", "Torso stays more upright.", "Squat to depth you can own."]),
    ("Goblet Squat", [G], "Dumbbell", "Beginner", ["Hold the bell at the chest.", "Elbows inside the knees at the bottom.", "Stand without the heels lifting."]),
    ("Leg Press", [G], "Machine", "Beginner", ["Feet mid-platform.", "Lower until the knees are near 90 degrees.", "Press without locking hard."]),
    ("Leg Extension", [], "Machine", "Beginner", ["Pad sits on the lower shin.", "Straighten the knees.", "Lower slowly."]),
    ("Bulgarian Split Squat", [G], "Dumbbell", "Intermediate", ["Rear foot on a bench.", "Drop the back knee.", "Front heel stays down."]),
    ("Walking Lunge", [G], "Dumbbell", "Beginner", ["Take a long step.", "Back knee travels toward the floor.", "Drive through the front heel."]),
    ("Hack Squat", [G], "Machine", "Intermediate", ["Shoulders under the pads.", "Squat down with the back on the pad.", "Press up evenly."]),
    ("Sissy Squat", [], "Bodyweight", "Advanced", ["Knees travel forward.", "Torso leans back with them.", "Use a support until you own it."]),
    ("Step-Up", [G], "Dumbbell", "Beginner", ["Whole foot on the box.", "Drive up without pushing off the back leg.", "Stand tall on the box."]),
    ("Heel-Elevated Squat", [G], "Dumbbell", "Intermediate", ["Heels on a small plate.", "Stay upright.", "Knees travel forward."]),
    ("Spanish Squat", [], "Bands", "Beginner", ["Band behind the knees, anchored low.", "Sit straight down.", "The band helps the knees track."]),
    ("Box Squat", [G], "Barbell", "Intermediate", ["Sit back to a box.", "Pause without relaxing.", "Stand up hard."]),
    ("Cyclist Squat", [], "Dumbbell", "Intermediate", ["Heels elevated, narrow stance.", "Stay very upright.", "Short range, high quad tension."]),
    ("Wall Sit", [], "Bodyweight", "Beginner", ["Back flat on the wall.", "Thighs near parallel.", "Hold and breathe."]),
])
data += group("Hamstrings", [
    ("Romanian Deadlift", [G], "Barbell", "Intermediate", ["Soft knees stay soft.", "Hinge until the hamstrings stretch.", "Stand by driving the hips through."]),
    ("Stiff-Leg Deadlift", [G], "Barbell", "Advanced", ["Less knee bend than an RDL.", "Bar stays close.", "Stop when the back wants to round."]),
    ("Lying Leg Curl", [], "Machine", "Beginner", ["Hips stay down.", "Curl the heels to the glutes.", "Lower under control."]),
    ("Seated Leg Curl", [], "Machine", "Beginner", ["Pad sits above the heels.", "Curl down and back.", "Don't let the hips lift."]),
    ("Nordic Curl", [], "Bodyweight", "Advanced", ["Anchor the ankles.", "Lower the body slowly.", "Catch yourself with the hands if needed."]),
    ("Good Morning", [G], "Barbell", "Advanced", ["Bar on the back, knees soft.", "Hinge the hips back.", "Return to a tall stand."]),
    ("Single-Leg Romanian Deadlift", [G], "Dumbbell", "Intermediate", ["Hinge on one leg.", "Hips stay square.", "Stand tall on the working leg."]),
    ("Glute-Ham Raise", [G], "Machine", "Advanced", ["Start with the body straight.", "Curl the heels and extend the hips.", "Lower slowly."]),
    ("Slider Leg Curl", [G], "Bodyweight", "Intermediate", ["Heels on sliders, hips up.", "Curl the heels in.", "Keep the hips high."]),
    ("Swiss-Ball Leg Curl", [G], "Other", "Intermediate", ["Heels on the ball.", "Curl it toward you.", "Don't let the hips drop."]),
    ("Dumbbell Romanian Deadlift", [G], "Dumbbell", "Beginner", ["Bells in front of the thighs.", "Hinge with a flat back.", "Stand tall."]),
    ("45-Degree Back Extension", [G], "Machine", "Beginner", ["Pad at the hips.", "Lower the torso.", "Raise until the body is straight, not past it."]),
    ("Standing Leg Curl", [], "Machine", "Beginner", ["Thigh stays on the pad.", "Curl the heel up.", "Lower slowly."]),
    ("Deficit Romanian Deadlift", [G], "Barbell", "Advanced", ["Stand on a small plate.", "Hinge a little deeper.", "Keep the bar close."]),
    ("Kettlebell Romanian Deadlift", [G], "Kettlebell", "Beginner", ["Bell close to the body.", "Hinge to a hamstring stretch.", "Stand by squeezing the glutes."]),
])
data += group("Glutes", [
    ("Hip Thrust", [H], "Barbell", "Intermediate", ["Upper back on a bench.", "Drive through the heels.", "Ribs stay down at the top.", "Pause when the hips are tall."]),
    ("Glute Bridge", [H], "Bodyweight", "Beginner", ["Feet flat, knees bent.", "Lift the hips.", "Squeeze without arching the lower back."]),
    ("Cable Kickback", [], "Cable", "Beginner", ["Slight forward lean.", "Kick the heel back.", "Don't swing the torso."]),
    ("Frog Pump", [], "Bodyweight", "Beginner", ["Soles of the feet together.", "Lift the hips in a small range.", "Squeeze at the top."]),
    ("Sumo Deadlift", [H, Q], "Barbell", "Advanced", ["Wide stance, toes out.", "Grip inside the knees.", "Push the floor apart and stand."]),
    ("Cable Pull-Through", [H], "Cable", "Beginner", ["Face away from the stack.", "Hinge and let the cable pull the hips back.", "Stand tall and squeeze."]),
    ("Lateral Band Walk", [], "Bands", "Beginner", ["Band above the knees.", "Sit into a small squat.", "Step sideways without letting the knees cave."]),
    ("Donkey Kick", [], "Bodyweight", "Beginner", ["On all fours.", "Kick the heel toward the ceiling.", "Hips stay square."]),
    ("Reverse Lunge", [Q], "Dumbbell", "Beginner", ["Step backward.", "Drop the back knee.", "Drive through the front heel."]),
    ("Single-Leg Hip Thrust", [H], "Bodyweight", "Intermediate", ["Shoulders on a bench.", "One foot planted.", "Drive that hip up and pause."]),
    ("Hip Abduction Machine", [], "Machine", "Beginner", ["Sit tall.", "Press the pads apart.", "Control the return."]),
    ("Curtsy Lunge", [Q], "Dumbbell", "Intermediate", ["Step one foot behind and across.", "Drop straight down.", "Keep the chest up."]),
    ("Kettlebell Swing", [H], "Kettlebell", "Intermediate", ["Hinge, don't squat deep.", "Snap the hips.", "Bell floats to chest height."]),
    ("Smith Machine Hip Thrust", [H], "Machine", "Intermediate", ["Bar across the hips.", "Drive up and pause.", "Don't overarch."]),
    ("Glute Kickback Machine", [], "Machine", "Beginner", ["Hip on the pad.", "Press the foot back.", "Squeeze at the end range."]),
])
data += group("Calves", [
    ("Standing Calf Raise", [], "Machine", "Beginner", ["Balls of the feet on the edge.", "Rise all the way up.", "Lower the heels below the step."]),
    ("Seated Calf Raise", [], "Machine", "Beginner", ["Pads on the knees.", "Lift the heels.", "Pause at the top and the bottom."]),
    ("Leg Press Calf Raise", [], "Machine", "Beginner", ["Balls of the feet on the bottom of the platform.", "Press through the toes.", "Don't lock and bounce."]),
    ("Donkey Calf Raise", [], "Machine", "Intermediate", ["Hinge at the hips.", "Raise the heels.", "Full stretch at the bottom."]),
    ("Single-Leg Calf Raise", [], "Bodyweight", "Beginner", ["Hold a support.", "Rise on one foot.", "Slow on the way down."]),
    ("Smith Machine Calf Raise", [], "Machine", "Intermediate", ["Bar on the back, toes on a plate.", "Rise and lower.", "Stay balanced."]),
    ("Tibialis Raise", [], "Bodyweight", "Beginner", ["Heels on the floor, toes up.", "Lift the toes toward the shins.", "Pause at the top."]),
    ("Dumbbell Calf Raise", [], "Dumbbell", "Beginner", ["Bell in one hand, other hand on a wall.", "Rise onto the toes.", "Full range."]),
    ("Bodyweight Calf Raise", [], "Bodyweight", "Beginner", ["Stand on a step.", "Up, pause, down.", "Both feet together."]),
    ("Eccentric Calf Drop", [], "Bodyweight", "Intermediate", ["Rise on two feet.", "Lower on one for a slow count.", "Use a step for range."]),
    ("Seated Dumbbell Calf Raise", [], "Dumbbell", "Beginner", ["Bells rest on the knees.", "Lift the heels.", "Keep the toes forward."]),
    ("Hack Squat Calf Raise", [], "Machine", "Intermediate", ["Toes on the platform.", "Press through the calves.", "Control the stretch."]),
    ("Band Calf Raise", [], "Bands", "Beginner", ["Band under the feet, held in the hands.", "Rise against the band.", "Slow lower."]),
    ("Farmer Calf Raise", [F], "Dumbbell", "Intermediate", ["Hold the bells at the sides.", "Raise the heels.", "Stay tall."]),
    ("Stair Calf Walk", [], "Bodyweight", "Beginner", ["Walk up on the balls of the feet.", "Don't bounce.", "Use a rail if you need it."]),
])
data += group("Abs/Core", [
    ("Plank", [], "Bodyweight", "Beginner", ["Elbows under the shoulders.", "Ribs and hips level.", "Squeeze the glutes and breathe."]),
    ("Dead Bug", [], "Bodyweight", "Beginner", ["Low back stays gently down.", "Reach the opposite arm and leg.", "Move slowly."]),
    ("Hanging Leg Raise", [], "Bodyweight", "Intermediate", ["Hang tall.", "Lift the legs without swinging.", "Lower until the body is long."]),
    ("Cable Crunch", [], "Cable", "Intermediate", ["Kneel facing the stack.", "Crunch the ribs toward the hips.", "Don't pull with the arms."]),
    ("Ab Wheel", [], "Other", "Advanced", ["Start on the knees.", "Roll out until the hips want to sag.", "Pull back with the abs."]),
    ("Bicycle Crunch", [], "Bodyweight", "Beginner", ["Shoulder toward the opposite knee.", "The other leg stays long.", "Slow, don't yank the neck."]),
    ("Russian Twist", [], "Bodyweight", "Beginner", ["Lean back slightly.", "Rotate the ribs, not just the arms.", "Feet down if the back tires."]),
    ("Pallof Press", [], "Cable", "Intermediate", ["Stand side-on to the cable.", "Press the handle straight out.", "Don't let the cable rotate you."]),
    ("Mountain Climber", [], "Bodyweight", "Beginner", ["Plank position.", "Drive one knee in, then the other.", "Hips stay low."]),
    ("Lying Leg Raise", [], "Bodyweight", "Beginner", ["Hands under the hips if needed.", "Lift the legs to vertical.", "Lower without the back arching hard."]),
    ("Side Plank", [], "Bodyweight", "Beginner", ["Elbow under the shoulder.", "Hips up.", "Body is a straight line."]),
    ("Cable Woodchop", [], "Cable", "Intermediate", ["Start high.", "Rotate down across the body.", "Hips and ribs turn together."]),
    ("V-Up", [], "Bodyweight", "Intermediate", ["Arms and legs meet over the hips.", "Lower with control.", "Keep the lower back honest."]),
    ("Hollow Hold", [], "Bodyweight", "Intermediate", ["Low back pressed down.", "Arms and legs reach long.", "Hold and breathe."]),
    ("Reverse Crunch", [], "Bodyweight", "Beginner", ["Knees bent.", "Curl the hips off the floor.", "Don't swing the legs."]),
])
data += group("Full Body", [
    ("Burpee", [Q, "Chest"], "Bodyweight", "Intermediate", ["Squat to the hands.", "Step or jump to a plank.", "Return and stand.", "Add a jump only if the landing is quiet."]),
    ("Thruster", [S, Q], "Barbell", "Advanced", ["Front squat.", "Drive straight into an overhead press.", "One smooth rep."]),
    ("Clean and Press", [S, B], "Barbell", "Advanced", ["Pull the bar in close.", "Catch it on the shoulders.", "Press overhead."]),
    ("Kettlebell Snatch", [S], "Kettlebell", "Advanced", ["Hinge and hike the bell.", "Punch through at the top.", "The bell rests on the forearm, not the wrist."]),
    ("Devil Press", [S, B], "Dumbbell", "Advanced", ["Burpee with two bells.", "Swing them overhead as you stand.", "Land softly."]),
    ("Turkish Get-Up", [S], "Kettlebell", "Advanced", ["Eyes on the bell.", "Move from the floor to standing in steps.", "Reverse the same path down."]),
    ("Dumbbell Snatch", [S], "Dumbbell", "Intermediate", ["One bell between the feet.", "Pull and punch overhead.", "Stand tall to finish."]),
    ("Squat to Press", [S, Q], "Dumbbell", "Beginner", ["Bells at the shoulders.", "Squat.", "Press as you stand."]),
    ("Renegade Row", [B, A], "Dumbbell", "Intermediate", ["Plank on the bells.", "Row one bell to the hip.", "Hips stay square."]),
    ("Man Maker", [S, B], "Dumbbell", "Advanced", ["Push-up, row each side, then squat to press.", "Keep the reps smooth.", "Use lighter bells than you row."]),
    ("Bear Complex", [S, B], "Barbell", "Advanced", ["Clean, front squat, push press, back squat, push press.", "One cycle, no rest.", "Learn it light."]),
    ("Dumbbell Clean", [B], "Dumbbell", "Intermediate", ["Bells start by the shins.", "Pull and catch at the shoulders.", "Stand tall."]),
    ("Sandbag Clean", [B, Q], "Other", "Advanced", ["Hug the bag.", "Extend the hips.", "Catch it in the arms at the chest."]),
    ("Wall Ball", [S, Q], "Other", "Intermediate", ["Squat with the ball.", "Throw it to a target as you stand.", "Catch and sit again."]),
    ("Farmer Carry Complex", [F, A], "Dumbbell", "Beginner", ["Carry, then shrug, then a short march.", "Stay tall the whole time.", "Switch grips if needed."]),
])
data += group("Cardio", [
    ("Treadmill Run", [], "Machine", "Beginner", ["Start with a walk.", "Land under the hips.", "Stop if form falls apart."]),
    ("Incline Walk", [], "Machine", "Beginner", ["Set a steep grade.", "Short steps, arms swinging.", "Don't hold the rails."]),
    ("Rowing Machine", [B], "Machine", "Intermediate", ["Legs, then hips, then arms.", "Return arms, hips, then knees.", "Don't round the back at the catch."]),
    ("Assault Bike", [Q], "Machine", "Intermediate", ["Push and pull the handles.", "Keep a rhythm you can hold.", "Breathe on purpose."]),
    ("Jump Rope", [CA], "Other", "Beginner", ["Small jumps.", "Wrists turn the rope.", "Stay on the balls of the feet."]),
    ("Stationary Bike", [Q], "Machine", "Beginner", ["Seat at hip height.", "Smooth circles.", "Don't collapse onto the bars."]),
    ("Stair Climber", [G, Q], "Machine", "Beginner", ["Light hands on the rails.", "Full steps.", "Stand tall."]),
    ("SkiErg", [B, A], "Machine", "Intermediate", ["Reach tall.", "Crack the hips down.", "Arms finish by the thighs."]),
    ("Jumping Jacks", [S], "Bodyweight", "Beginner", ["Soft landings.", "Arms overhead.", "Keep a steady pace."]),
    ("High Knees", [Q], "Bodyweight", "Beginner", ["Knees drive up.", "Stay on the forefoot.", "Quick, quiet feet."]),
    ("Elliptical", [Q], "Machine", "Beginner", ["Tall posture.", "Push and pull the handles.", "Don't bounce."]),
    ("Shadow Boxing", [S], "Bodyweight", "Beginner", ["Hands up.", "Turn the hips with the punch.", "Breathe out on each strike."]),
    ("Battle Ropes", [S, A], "Other", "Intermediate", ["Athletic stance.", "Make even waves.", "Don't hunch."]),
    ("Box Step", [Q, G], "Bodyweight", "Beginner", ["Step up and down one foot at a time.", "Full foot on the box.", "Quiet landings."]),
    ("Pool Laps", [], "Other", "Intermediate", ["Long body line.", "Exhale underwater.", "Rest at the wall if the stroke breaks."]),
])

# unique ids and names
ids = [row["id"] for row in data]
names = [row["name"] for row in data]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
assert len(names) == len(set(names))
from collections import Counter
print(Counter(row["primary"] for row in data))
print("TOTAL", len(data))
Path(__file__).with_name("exercises.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
