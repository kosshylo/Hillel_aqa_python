from lesson_16.homework_16_1.Employee import TeamLead, Developer

def test_teamlead_inherits_attributes_and_initial_team_size_is_zero():
    lead = TeamLead("Kostia", 50000, "Embedded", "Python")

    # Validation avalability all inherits attributes
    assert hasattr(lead, "name")
    assert hasattr(lead, "salary")
    assert hasattr(lead, "department")
    assert hasattr(lead, "programming_language")

    # Start size of team is 0
    assert lead.return_team_size() == 0

    # Add dev and validate team_size
    dev1 = Developer("Volodia", 37000, "Python")
    lead.add_developer(dev1)

    assert lead.return_team_size() == 1

    # Add dev2 and validate team_size
    dev2 = Developer("Tania", 37000, "Python")
    lead.add_developer(dev2)

    assert lead.return_team_size() == 2