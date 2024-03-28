def particles_in_event(event):
    "Gives a generator for particles given an event"
    return (event.product()[0].GetParticle(i) for i in range(num_particles(event)))


def pdg_code(particle):
    "Particle attribute"
    return particle.PdgCode()


def pdg_codes(event):
    "Event attribute"
    particles = particles_in_event(event)
    return list(map(pdg_code, particles))


def num_particles(event):
    "Event attribute"
    return event.product()[0].NParticles()
