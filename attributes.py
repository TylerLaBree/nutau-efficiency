def particles_in_event(event):
    "Gives a generator for particles given an event"
    return (event.product()[0].GetParticle(i) for i in range(num_particles(event)))


def pdg_codes(event):
    return [particle.PdgCode() for particle in particles_in_event(event)]


def energies(event):
    return [
        [particle.Momentum()[j] for j in range(4)][3]
        for particle in particles_in_event(event)
    ]


def four_momentums(event):
    return [
        [particle.Momentum()[j] for j in range(4)]
        for particle in particles_in_event(event)
    ]


def num_particles(event):
    return event.product()[0].NParticles()


def num_leptons(event):
    """
    Machado N_lep
    Returns number of (anti)electrons and (anti)muons
    """

    def is_lepton(code):
        return code in [11, -11, 13, -13]

    return sum(map(int, map(is_lepton, pdg_codes(event))))


def num_pions(event):
    """
    Machado N_{\pi^-}
    Returns number of negative pions.
    He says later that we may not be able to discriminate positive and negative pions.
    """

    def is_pion(code):
        return code in [211]

    return sum(map(int, map(is_pion, pdg_codes(event))))


def leading_pion_energies(event):
    """
    Machado \pi^-_lead
    Returns the energy of the leading pion
    """

    def is_pion(code):
        return code in [211]

    return max([energy for (energy, is_pion_val) in zip(energies(event), map(is_pion, pdg_codes(event))) if is_pion_val], default=0)
