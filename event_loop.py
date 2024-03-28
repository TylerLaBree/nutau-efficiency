import ROOT


def read_header(h):
    "Make the ROOT C++ jit compiler read the specified header."
    ROOT.gROOT.ProcessLine('#include "%s"' % h)


def provide_get_valid_handle(klass):
    """
    Make the ROOT C++ jit compiler instantiate the
    Event::getValidHandle member template for template
    parameter klass.
    """
    ROOT.gROOT.ProcessLine(
        "template gallery::ValidHandle<%(name)s> gallery::Event::getValidHandle<%(name)s>(art::InputTag const&) const;"
        % {"name": klass}
    )


def read_attribute(filename, attribute, sample_size=10):
    mctruths_tag = ROOT.art.InputTag("generator")
    filenames = ROOT.vector(ROOT.string)(1, filename)
    events = ROOT.gallery.Event(filenames)
    get_mctruths = events.getValidHandle[ROOT.vector(ROOT.simb.MCTruth)]
    count = 0
    acc = []
    while not events.atEnd():
        event = get_mctruths(mctruths_tag)
        if count >= sample_size or event.empty():
            break
        count += 1
        acc.append(attribute(event))
        events.next()
    return acc


def dump_events(filename, sample_size=10):
    mctruths_tag = ROOT.art.InputTag("generator")
    filenames = ROOT.vector(ROOT.string)(1, filename)
    events = ROOT.gallery.Event(filenames)
    get_mctruths = events.getValidHandle[ROOT.vector(ROOT.simb.MCTruth)]
    count = 0

    def star_if_true(criterion):
        return "*" if criterion else ""

    while not events.atEnd():
        event = get_mctruths(mctruths_tag)
        if count >= sample_size or event.empty():
            break
        count += 1
        num_particles = event.product()[0].NParticles()
        print()
        print("num_particles:", num_particles)

        particles = (event.product()[0].GetParticle(i) for i in range(num_particles))
        for particle in particles:
            pdg_code = particle.PdgCode()
            print("pgd_code:", pdg_code, star_if_true(pdg_code in important_particles))
            four_momentum = [particle.Momentum()[j] for j in range(4)]
            print("energy:", four_momentum[3])
        events.next()
