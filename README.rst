============
Zope Cooties
============

Popularity has its price. Tired of having to review pull requests, answer
questions about your code, participate in Reddit discussions, all to support
open source software that you've given to the world for free?  Now you can send
potential new users heading for the hills with a simple addition to the
`install_requires` in your `setup.py`.  Depending on this package will cause
the word `Zope` to appear on the screen while your package is being installed,
thus dramatically reducing the support burden for releasing open source
software.

All you have to do is depend on `zope.cooties` and your project will obtain
transitive dependencies on two different Zope packages chosen at random at
install time, as well as any of their dependencies.  Suddenly your users will
be installing ZODB or the ZCA for no apparent reason just to use your code. 

Try it today and give the haters more to hate.
