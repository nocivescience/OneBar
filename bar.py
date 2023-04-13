from manim import *
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
        values=[1,2,3,4,5,6,7,8,9,10]
        # bar.add_updater(lambda b:self.set_bar(b,line_number,value_tracker.get_value()))
        self.add(line_number,bar)
        bar.add_updater(lambda b:b.stretch_to_fit_width(value_tracker.get_value()*line_number.x_range[-1],about_edge=LEFT))
        self.play(value_tracker.animate.set_value(10),run_time=10)
        # for value in values:
        #     anims=[ApplyMethod(bar.stretch_to_fit_width,value*line_number.x_range[-1],about_edge=LEFT)]
        #     self.play(*anims)
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