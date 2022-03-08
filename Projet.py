from pycsp3 import *

V , E = data


satisfy(

    AllDifferent(f)

    minimize(
        Maximum(Minimum(abs(f(v)-f(u)),len(V)-abs(f(v)-f(u))))
    )
)