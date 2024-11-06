% Clear workspace and command window
clear all;
clc;

% Parameters
image_path = 'halley.jpg'; 
elements_x = 4;
elements_y = 4;
max_error = 1;
show_edges = true;
max_refinement_level = 12;

% 1. Full RGB adaptation
fprintf('Running full RGB adaptation...\n');
bitmap_h(image_path, elements_x, elements_y, max_error, max_refinement_level, show_edges, sprintf('full_rgb/refinement_level_%d.jpg', max_refinement_level));


% 2. Red channel adaptation
fprintf('Running red channel adaptation...\n');
bitmap_h_red(image_path, elements_x, elements_y, max_error, max_refinement_level, show_edges, sprintf('red_channel/refinement_level_%d.jpg', max_refinement_level));

% 3. Green channel adaptation
fprintf('Running green channel adaptation...\n');
bitmap_h_green(image_path, elements_x, elements_y, max_error, max_refinement_level, show_edges, sprintf('green_channel/refinement_level_%d.jpg', max_refinement_level));

% 4. Blue channel adaptation
fprintf('Running blue channel adaptation...\n');
bitmap_h_blue(image_path, elements_x, elements_y, max_error, max_refinement_level, show_edges, sprintf('blue_channel/refinement_level_%d.jpg', max_refinement_level));
