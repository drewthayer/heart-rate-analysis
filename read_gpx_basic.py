from lxml import etree
import numpy as np

if __name__=='__main__':
    file = 'data/activity_2572056251.gpx'

    gpx = etree.parse(file)

    namespace = "http://www.topografix.com/GPX/1/1"

    # get name
    tag='name'
    name_elem = gpx.xpath("//gpx:{}".format(tag), namespaces = {'gpx': namespace})
    name = [e.text for e in name_elem]

    # get type
    tag = 'type'
    type_elem = gpx.xpath("//gpx:{}".format(tag), namespaces = {'gpx': namespace})
    type = [e.text for e in type_elem]

    # get elevations
    elev_elems = gpx.xpath("//gpx:ele", namespaces = {'gpx': namespace})
    elevs = np.array([float(e.text) for e in elev_elems])

    # get times
    t_elems = gpx.xpath("//gpx:time", namespaces = {'gpx': namespace})
    times = [e.text for e in t_elems]

    # get heartrates
    hr_elems = gpx.xpath("//*[name()='ns3:hr']", namespaces = {'gpx': namespace})
    hrs = np.array([int(e.text) for e in hr_elems])
