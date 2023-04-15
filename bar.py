from manim import *
import itertools as it
class Bar(Scene):
    CONFIG={
        'line_config':{
            'x_range':[0,10,1],
            'include_numbers':True,
        },
    }
    def construct(self):
        line_number=NumberLine(**self.CONFIG['line_config'])
        bar=self.get_bar(line_number)
        value_tracker=ValueTracker(1)
        indice=self.get_data()
        self.add(line_number,bar,indice)
        bar.add_updater(lambda b:b.stretch_to_fit_width(value_tracker.get_value()*line_number.x_range[-1],about_edge=LEFT))
        indice[1].add_updater(lambda i:i.set_value(value_tracker.get_value()))
        values=np.array([self.get_randon_value() for i in range(10)])
        np.random.shuffle(values)
        value_cycle=list(it.islice(it.cycle(values),0,200))
        np.random.shuffle(value_cycle)
        for value in value_cycle:
            self.play(ApplyMethod(value_tracker.set_value,value),run_time=.1)
        self.wait()
    def get_bar(self,line):
        bar=Rectangle(height=.3,width=line.x_range[-1]*2)
        bar.move_to(line.number_to_point(0),aligned_edge=LEFT) 
        return bar
    def set_bar(self,bar,line,value):
        bar.set_width(line.number_to_point(value))
        bar.move_to(line.number_to_point(0),aligned_edge=LEFT)
        bar.stretch_to_fit_width(
            value*line.x_range[-1],
            about_edge=LEFT
        )
        return bar
    def get_randon_value(self):
        return np.random.randint(1,10)
    def get_data(self):
        indice=VGroup(
            Tex('Indice'),
            Integer(0)
        )
        indice.align_to(indice[0],DOWN)
        indice.arrange(RIGHT)
        indice.move_to(UP*2)
        return indice